const catalog = window.ENCYCLOPEDIA_CATALOG || { entries: [] };
window.ENCYCLOPEDIA_ENTRY_BODIES = window.ENCYCLOPEDIA_ENTRY_BODIES || {};
const provenanceCatalog = catalog.provenanceCatalog || {};
const chapterScopeCatalog = catalog.chapterScopeCatalog || {};
for (const entry of catalog.entries) {
  const generatedSearchText = entry.searchText;
  const fallbackSearchText = [
    entry.title,
    entry.kind,
    entry.summary,
    entry.provenance && provenanceLabel(entry.provenance),
    entry.chapterScope && chapterScopeLabel(entry.chapterScope),
    entry.aliases && entry.aliases.join(" "),
    entry.addresses && entry.addresses.join(" "),
    entry.banks && entry.banks.join(" "),
    entry.sourceRefs && entry.sourceRefs.map((ref) => `${ref.label || ""} ${ref.path || ""}`).join(" "),
    entry.noteRefs && entry.noteRefs.map((ref) => `${ref.label || ""} ${ref.path || ""}`).join(" "),
    entry.body
  ].filter(Boolean).join(" ");
  entry.searchText = String(generatedSearchText || fallbackSearchText).toLowerCase();
}
const entries = new Map(catalog.entries.map((entry) => [entry.id, entry]));
const referenceIndex = buildReferenceIndex();
const relationshipGraph = catalog.relationshipGraph || { stats: {}, nodes: [], edges: [], neighborhoods: {}, topHubs: [] };
const graphNodes = new Map((relationshipGraph.nodes || []).map((node) => [node.id, node]));
const ASM_MNEMONICS = new Set([
  "adc", "and", "asl", "bcc", "bcs", "beq", "bit", "bmi", "bne", "bpl", "bra", "brk", "brl", "bvc", "bvs",
  "clc", "cld", "cli", "clv", "cmp", "cop", "cpx", "cpy", "dec", "dex", "dey", "eor", "inc", "inx", "iny",
  "jmp", "jml", "jsl", "jsr", "lda", "ldx", "ldy", "lsr", "mvn", "mvp", "nop", "ora", "pea", "pei", "per",
  "pha", "phb", "phd", "phk", "php", "phx", "phy", "pla", "plb", "pld", "plp", "plx", "ply", "rep", "rol",
  "ror", "rti", "rtl", "rts", "sbc", "sec", "sed", "sei", "sep", "sta", "stp", "stx", "sty", "stz", "tax",
  "tay", "tcd", "tcs", "tdc", "trb", "tsb", "tsc", "tsx", "txa", "txs", "txy", "tya", "tyx", "wai", "wdm",
  "xba", "xce"
]);
const ASM_KEYWORDS = new Set([
  "arch", "base", "db", "dl", "dw", "endmacro", "endif", "fill", "if", "incbin", "macro", "namespace",
  "org", "pad", "pushpc", "pullpc", "rep", "warnpc"
]);

const FULL_RESULTS_LIMIT = 1000;
const NAV_STATE_KEY = "earthbound-encyclopedia-nav-v1";
const LOCAL_WORKSPACE_STATE_KEY = "earthbound-encyclopedia-local-workspace-v1";
const FIRST_RUN_STATE_KEY = "earthbound-encyclopedia-first-run-dismissed-v1";
const FAVORITES_STATE_KEY = "earthbound-encyclopedia-favorites-v1";
const state = {
  tabs: ["overview"],
  activeId: "overview",
  graphFocusId: "overview",
  railTab: "outline",
  localWorkspace: loadLocalWorkspaceState(),
  firstRunDismissed: loadFirstRunDismissed(),
  workspaceMessage: "",
  workspaceFilePreviews: {},
  workspaceMediaPreviews: {},
  assetBrowser: {
    graphicsBank: "all",
    graphicsShowAll: false
  }
};
const KIND_ORDER = [
  "chapter",
  "learning-path",
  "narrative",
  "bank",
  "topic",
  "script-vm",
  "text-command",
  "asset-contract",
  "asset-manifest",
  "asset",
  "source",
  "source-file",
  "symbol",
  "routine",
  "tool",
  "note",
  "workflow",
  "search"
];

const tocEl = document.getElementById("toc");
const tabsEl = document.getElementById("tabs");
const documentEl = document.getElementById("documentView");
const railEl = document.getElementById("detailsRail");
const searchInput = document.getElementById("globalSearch");
const searchResults = document.getElementById("searchResults");
const backButton = document.getElementById("backButton");
const forwardButton = document.getElementById("forwardButton");
const workspaceButton = document.getElementById("workspaceButton");
const buildStatusButton = document.getElementById("buildStatusButton");
let currentDocumentOutline = [];
let currentSearchResults = [];
let searchSelectionIndex = 0;
state.favorites = loadFavoriteIds();
state.scrollPositions = {};
state.pendingScroll = null;
if ("scrollRestoration" in window.history) {
  window.history.scrollRestoration = "manual";
}

const initialTarget = parseLocationTarget();
if (initialTarget.id && entries.has(initialTarget.id)) {
  state.tabs = [initialTarget.id];
  state.activeId = initialTarget.id;
  state.pendingScroll = initialTarget.sectionId
    ? { type: "section", id: initialTarget.sectionId, behavior: "auto", attempts: 0 }
    : { type: "top" };
} else {
  restoreWorkspaceState();
}

function entryLabel(entry) {
  return entry ? entry.title : "Missing entry";
}

function loadFavoriteIds() {
  try {
    const raw = window.localStorage.getItem(FAVORITES_STATE_KEY);
    const ids = raw ? JSON.parse(raw) : [];
    return Array.isArray(ids)
      ? ids.filter((id, index, list) => entries.has(id) && list.indexOf(id) === index)
      : [];
  } catch (error) {
    window.localStorage.removeItem(FAVORITES_STATE_KEY);
    return [];
  }
}

function saveFavoriteIds() {
  try {
    window.localStorage.setItem(FAVORITES_STATE_KEY, JSON.stringify(state.favorites));
  } catch (error) {
    // Favorites are a convenience layer; the app still works if storage is unavailable.
  }
}

function loadLocalWorkspaceState() {
  try {
    const raw = window.localStorage.getItem(LOCAL_WORKSPACE_STATE_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch (error) {
    window.localStorage.removeItem(LOCAL_WORKSPACE_STATE_KEY);
    return null;
  }
}

function saveLocalWorkspaceState(value) {
  state.localWorkspace = value;
  try {
    if (value) {
      window.localStorage.setItem(LOCAL_WORKSPACE_STATE_KEY, JSON.stringify(value));
    } else {
      window.localStorage.removeItem(LOCAL_WORKSPACE_STATE_KEY);
    }
  } catch (error) {
    // Workspace metadata is a convenience cache; Electron stores the durable manifest.
  }
}

function loadFirstRunDismissed() {
  try {
    return window.localStorage.getItem(FIRST_RUN_STATE_KEY) === "true";
  } catch (error) {
    return false;
  }
}

function saveFirstRunDismissed(value) {
  state.firstRunDismissed = Boolean(value);
  try {
    window.localStorage.setItem(FIRST_RUN_STATE_KEY, state.firstRunDismissed ? "true" : "false");
  } catch (error) {
    // The prompt can reappear if storage is unavailable.
  }
}

function workspaceIsReady() {
  return Boolean(state.localWorkspace?.rom?.sha1Ok || state.localWorkspace?.manifest?.rom?.sha1Ok);
}

function isFavorite(id) {
  return state.favorites.includes(id);
}

function toggleFavorite(id) {
  if (!entries.has(id)) {
    return;
  }
  saveActiveScrollPosition();
  if (isFavorite(id)) {
    state.favorites = state.favorites.filter((favoriteId) => favoriteId !== id);
  } else {
    state.favorites = [id, ...state.favorites.filter((favoriteId) => favoriteId !== id)];
    state.railTab = "favorites";
  }
  saveFavoriteIds();
  render();
}

function openEntry(id, options = {}) {
  if (!entries.has(id)) {
    return;
  }
  saveActiveScrollPosition();
  const openInNewTab = Boolean(options.newTab || options.event?.ctrlKey);
  const sectionId = options.sectionId || "";
  const pushHistory = options.pushHistory !== false;
  if (pushHistory && (id !== state.activeId || sectionId)) {
    state.backStack = state.backStack || [];
    state.forwardStack = [];
    state.backStack.push(activeScrollSnapshot());
  }

  if (openInNewTab) {
    if (!state.tabs.includes(id)) {
      state.tabs.push(id);
    }
  } else if (!state.tabs.includes(id)) {
    const activeIndex = Math.max(0, state.tabs.indexOf(state.activeId));
    state.tabs[activeIndex] = id;
  }

  if (!state.tabs.length) {
    state.tabs.push(id);
  }
  state.activeId = id;
  state.pendingScroll = scrollIntentFromOptions(options, sectionId);
  updateLocation(id, sectionId);
  render();
}

function goBack() {
  if (!state.backStack || !state.backStack.length) {
    return;
  }
  saveActiveScrollPosition();
  state.forwardStack = state.forwardStack || [];
  state.forwardStack.push(activeScrollSnapshot());
  navigateToSnapshot(state.backStack.pop());
}

function goForward() {
  if (!state.forwardStack || !state.forwardStack.length) {
    return;
  }
  saveActiveScrollPosition();
  state.backStack = state.backStack || [];
  state.backStack.push(activeScrollSnapshot());
  navigateToSnapshot(state.forwardStack.pop());
}

function closeTab(id, event) {
  event.stopPropagation();
  if (state.tabs.length === 1) {
    return;
  }
  const index = state.tabs.indexOf(id);
  state.tabs = state.tabs.filter((tabId) => tabId !== id);
  if (state.activeId === id) {
    state.activeId = state.tabs[Math.max(0, index - 1)];
    state.pendingScroll = { type: "position", top: state.scrollPositions[state.activeId] || 0 };
    updateLocation(state.activeId);
  }
  render();
}

function activeScrollSnapshot() {
  return {
    id: state.activeId,
    scrollTop: documentEl ? documentEl.scrollTop || 0 : 0
  };
}

function saveActiveScrollPosition() {
  if (state.activeId && documentEl) {
    state.scrollPositions[state.activeId] = documentEl.scrollTop || 0;
  }
}

function navigateToSnapshot(snapshot) {
  const target = normalizeNavigationSnapshot(snapshot);
  if (!target || !entries.has(target.id)) {
    return;
  }
  if (!state.tabs.includes(target.id)) {
    const activeIndex = Math.max(0, state.tabs.indexOf(state.activeId));
    state.tabs[activeIndex] = target.id;
  }
  state.activeId = target.id;
  state.pendingScroll = { type: "position", top: target.scrollTop || 0 };
  updateLocation(target.id);
  render();
}

function normalizeNavigationSnapshot(snapshot) {
  if (typeof snapshot === "string") {
    return { id: snapshot, scrollTop: 0 };
  }
  if (snapshot && typeof snapshot === "object") {
    return snapshot;
  }
  return null;
}

function scrollIntentFromOptions(options, sectionId) {
  if (sectionId) {
    return { type: "section", id: sectionId, behavior: options.scrollBehavior || "auto", attempts: 0 };
  }
  if (Number.isFinite(options.scrollTop)) {
    return { type: "position", top: options.scrollTop };
  }
  if (options.restoreScroll) {
    return { type: "position", top: state.scrollPositions[options.id || state.activeId] || 0 };
  }
  return { type: "top" };
}

function parseLocationTarget() {
  const rawHash = decodeURIComponent(window.location.hash.replace(/^#/, ""));
  if (!rawHash) {
    return { id: "", sectionId: "" };
  }
  return parseEntryTarget(rawHash);
}

function parseEntryTarget(value) {
  const raw = String(value || "").trim();
  const separator = raw.includes("::") ? "::" : raw.includes("#") ? "#" : "";
  if (!separator) {
    return { id: raw, sectionId: "" };
  }
  const [id, ...sectionParts] = raw.split(separator);
  return { id, sectionId: sectionParts.join(separator) };
}

function updateLocation(id, sectionId = "") {
  const hash = sectionId ? `${id}::${sectionId}` : id;
  window.history.replaceState(null, "", `#${encodeURIComponent(hash)}`);
}

function restoreWorkspaceState() {
  try {
    const raw = window.localStorage.getItem(NAV_STATE_KEY);
    if (!raw) {
      return;
    }
    const saved = JSON.parse(raw);
    const tabs = Array.isArray(saved.tabs)
      ? saved.tabs.filter((id) => entries.has(id)).slice(0, 12)
      : [];
    if (tabs.length) {
      state.tabs = tabs;
    }
    if (saved.activeId && entries.has(saved.activeId)) {
      state.activeId = saved.activeId;
      if (!state.tabs.includes(saved.activeId)) {
        state.tabs.unshift(saved.activeId);
      }
    }
    if (saved.graphFocusId && entries.has(saved.graphFocusId)) {
      state.graphFocusId = saved.graphFocusId;
    }
    state.tabs = state.tabs.filter((id, index, list) => list.indexOf(id) === index);
    window.history.replaceState(null, "", `#${encodeURIComponent(state.activeId)}`);
  } catch (error) {
    window.localStorage.removeItem(NAV_STATE_KEY);
  }
}

function saveWorkspaceState() {
  try {
    window.localStorage.setItem(NAV_STATE_KEY, JSON.stringify({
      tabs: state.tabs,
      activeId: state.activeId,
      graphFocusId: state.graphFocusId
    }));
  } catch (error) {
    // Storage can be unavailable for local files in some locked-down environments.
  }
}

function groupEntries() {
  const groups = [
    ["Start", ["chapter", "workflow"]],
    ["Learning Paths", ["learning-path"]],
    ["Chapters", ["narrative"]],
    ["Topics", ["topic"]],
    ["Runtime", ["bank", "subsystem"]],
    ["Script And Text", ["text-command", "script-vm"]],
    ["Assets", ["asset-contract", "asset-manifest"]],
    ["Reference", ["source", "source-file", "symbol", "routine", "tool", "note", "search"]]
  ];

  return groups.map(([title, kinds]) => ({
    title,
    entries: catalog.entries
      .filter((entry) => kinds.includes(entry.kind) && entry.showInToc !== false)
      .sort((a, b) => (a.tocPriority ?? 50) - (b.tocPriority ?? 50) || a.title.localeCompare(b.title))
  })).filter((group) => group.entries.length > 0);
}

function renderToc() {
  tocEl.innerHTML = "";
  for (const group of groupEntries()) {
    const wrapper = document.createElement("section");
    wrapper.className = "tocGroup";
    const heading = document.createElement("div");
    heading.className = "tocGroupTitle";
    heading.textContent = group.title;
    wrapper.appendChild(heading);

    for (const entry of group.entries) {
      const button = document.createElement("button");
      button.className = `tocButton${entry.id === state.activeId ? " active" : ""}`;
      button.type = "button";
      button.innerHTML = `<span class="tocTitle">${escapeHtml(entry.title)}</span><span class="tocKind">${escapeHtml(entry.kind)}</span>`;
      bindEntryLinkButton(button, { entryId: entry.id });
      wrapper.appendChild(button);
    }
    tocEl.appendChild(wrapper);
  }
}

function renderTabs() {
  tabsEl.innerHTML = "";
  for (const id of state.tabs) {
    const entry = entries.get(id);
    const tab = document.createElement("button");
    tab.type = "button";
    tab.className = `tab${id === state.activeId ? " active" : ""}`;
    tab.addEventListener("click", () => {
      saveActiveScrollPosition();
      state.activeId = id;
      state.pendingScroll = { type: "position", top: state.scrollPositions[id] || 0 };
      updateLocation(id);
      render();
    });

    const close = state.tabs.length > 1
      ? `<span class="tabClose" data-close="${escapeHtml(id)}" title="Close">x</span>`
      : "";
    tab.innerHTML = `<span class="tabTitle">${escapeHtml(entryLabel(entry))}</span>${close}`;
    const closeButton = tab.querySelector(".tabClose");
    if (closeButton) {
      closeButton.addEventListener("click", (event) => closeTab(id, event));
    }
    tabsEl.appendChild(tab);
  }
}

function renderDocument() {
  const entry = entries.get(state.activeId);
  if (!entry) {
    documentEl.innerHTML = '<div class="emptyState">Entry not found.</div>';
    railEl.innerHTML = "";
    currentDocumentOutline = [];
    return;
  }

  currentDocumentOutline = [];
  documentEl.innerHTML = `
    <div class="docInner">
      ${renderFirstRunPrompt()}
      <div class="entryKind">${escapeHtml(entry.kind)}</div>
      <div class="titleRow">
        <h1>${escapeHtml(entry.title)}</h1>
        ${renderFavoriteButton(entry)}
      </div>
      ${renderMetaStrip(entry)}
      ${shouldRenderSummary(entry) ? `<p>${escapeHtml(entry.summary)}</p>` : ""}
      ${renderEntryBody(entry)}
      ${renderDeferredBodyLoader(entry)}
      ${renderReferenceWorkbench(entry)}
      ${entry.id === "relationship-graph" ? renderRelationshipGraphDocument() : renderEntryGraphPreview(entry)}
    </div>
  `;

  bindEntryLinkClicks(documentEl);
  documentEl.querySelectorAll("[data-favorite-id]").forEach((button) => {
    button.addEventListener("click", () => toggleFavorite(button.getAttribute("data-favorite-id")));
  });
  documentEl.querySelectorAll("[data-graph-focus-id]").forEach((button) => {
    button.addEventListener("click", () => {
      state.graphFocusId = button.getAttribute("data-graph-focus-id");
      render();
    });
  });
  documentEl.querySelectorAll("[data-open-graph-focus-id]").forEach((button) => {
    button.addEventListener("click", (event) => {
      state.graphFocusId = button.getAttribute("data-open-graph-focus-id");
      openEntry("relationship-graph", { event });
    });
  });
  documentEl.querySelectorAll("[data-load-body-id]").forEach((button) => {
    button.addEventListener("click", () => loadDeferredBody(button.getAttribute("data-load-body-id")));
  });
  documentEl.querySelectorAll("[data-workspace-action]").forEach((button) => {
    button.addEventListener("click", () => handleWorkspaceAction(button.getAttribute("data-workspace-action"), button));
  });
  documentEl.querySelectorAll("[data-workspace-file]").forEach((button) => {
    button.addEventListener("click", () => loadWorkspaceFilePreview(button));
  });
  documentEl.querySelectorAll("[data-workspace-media]").forEach((button) => {
    button.addEventListener("click", () => loadWorkspaceMediaPreview(button));
  });
  documentEl.querySelectorAll("[data-asset-browser-action]").forEach((button) => {
    button.addEventListener("click", () => handleAssetBrowserAction(button));
  });
  enhanceCodeBlocks();

  renderRail(entry);
  applyPendingScroll();
}

function shouldRenderSummary(entry) {
  if (!entry.summary) {
    return false;
  }
  const summary = normalizeSummaryText(entry.summary);
  const bodyStart = normalizeSummaryText(String(entry.body || "").slice(0, entry.summary.length + 120));
  return !bodyStart.startsWith(summary);
}

function renderFirstRunPrompt() {
  if (workspaceIsReady() || state.firstRunDismissed) {
    return "";
  }
  return `
    <section class="firstRunPrompt" aria-label="First run local workspace setup">
      <div>
        <strong>Add a ROM to prepare local source, asset, and audio generation.</strong>
        <div class="workspaceNotice">You can also skip this and browse the project-authored encyclopedia without ROM-derived generated material.</div>
      </div>
      <div class="firstRunActions">
        <button type="button" class="primaryAction" data-workspace-action="select-rom">Add ROM</button>
        <button type="button" class="secondaryAction" data-workspace-action="dismiss-first-run">Browse notes only</button>
        <button type="button" class="secondaryAction" data-entry-id="local-workspace">Local Workspace</button>
      </div>
    </section>
  `;
}

function renderFavoriteButton(entry) {
  const active = isFavorite(entry.id);
  return `
    <button type="button" class="favoriteButton${active ? " active" : ""}" data-favorite-id="${escapeHtml(entry.id)}" aria-pressed="${active ? "true" : "false"}" title="${active ? "Remove from favorites" : "Add to favorites"}">
      <span aria-hidden="true">${active ? "&#9733;" : "&#9734;"}</span>
    </button>
  `;
}

function normalizeSummaryText(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function renderEntryBody(entry) {
  if (entry.id === "local-workspace") {
    return `${renderMarkdown(entry.body || "", { collectHeadings: true })}${renderLocalWorkspacePanel()}`;
  }
  if (entry.id === "asset-library") {
    return `${renderMarkdown(entry.body || "", { collectHeadings: true })}${renderAssetLibraryPanel()}`;
  }
  if (/^source-bank-[c-e][0-9a-f]$/i.test(entry.id)) {
    return `${renderMarkdown(entry.body || "", { collectHeadings: true })}${renderGeneratedSourceBankPanel(entry)}`;
  }
  if (entry.id === "source-tree") {
    return `${renderMarkdown(entry.body || "", { collectHeadings: true })}${renderGeneratedSourceTreePanel()}`;
  }
  if (entry.id === "narrative-index") {
    return renderNarrativeHub();
  }
  if (entry.id === "learning-path-index") {
    return renderLearningPathIndex();
  }
  if (entry.id === "topic-index") {
    return renderTopicHub();
  }
  if (entry.id === "source-browser") {
    return renderSourceBrowserHub();
  }
  if (entry.learningPath) {
    return renderLearningPathGuide(entry);
  }
  return renderMarkdown(entry.body || "", { collectHeadings: true });
}

function renderNarrativeHub() {
  const headingCounts = new Map();
  const chapterId = registerHubSection("Curated Chapters", headingCounts);
  const learningId = registerHubSection("Guided Learning", headingCounts);
  const chapters = catalog.entries
    .filter((entry) => entry.kind === "narrative")
    .sort((a, b) => (a.tocPriority ?? 50) - (b.tocPriority ?? 50) || a.title.localeCompare(b.title));
  const learningPaths = catalog.entries
    .filter((entry) => entry.kind === "learning-path" && entry.id !== "learning-path-index" && entry.learningPath)
    .sort((a, b) => (a.tocPriority ?? 50) - (b.tocPriority ?? 50) || a.title.localeCompare(b.title));
  return `
    <section class="hubPage">
      <section class="hubSection" id="${escapeHtml(chapterId)}">
        <div class="hubSectionHeader">
          <h2>Curated Chapters</h2>
          <p>Human-maintained explanations enriched with generated evidence, notes, banks, and graph links.</p>
        </div>
        <div class="hubGrid">
          ${chapters.map((entry) => renderHubCard(entry, {
            eyebrow: maturityLabel(entry.maturity || "draft-narrative"),
            meta: evidenceMeta(entry),
            secondaryId: learningPathForChapter(entry),
            secondaryLabel: "Learning path"
          })).join("")}
        </div>
      </section>
      <section class="hubSection" id="${escapeHtml(learningId)}">
        <div class="hubSectionHeader">
          <h2>Guided Learning</h2>
          <p>Route-style walkthroughs that start from a chapter and fan out into primary evidence.</p>
        </div>
        <div class="hubGrid compact">
          ${learningPaths.map((entry) => renderHubCard(entry, {
            eyebrow: "Guided route",
            meta: learningPathMeta(entry),
            tags: entry.banks?.map((bank) => `Bank ${bank}`) || []
          })).join("")}
        </div>
      </section>
    </section>
  `;
}

function workspaceRom() {
  return state.localWorkspace?.manifest?.rom || state.localWorkspace?.rom || null;
}

function workspaceManifest() {
  return state.localWorkspace?.manifest || null;
}

function workspacePreviewKey(familyId, relativePath) {
  return `${familyId}:${relativePath}`;
}

function workspaceFamilyFiles(familyId) {
  const family = workspaceFamily(familyId);
  return Array.isArray(family?.files) ? family.files : [];
}

function sourceBankFromEntry(entry) {
  return String(entry?.banks?.[0] || entry?.id?.replace(/^source-bank-/i, "") || "").toLowerCase();
}

function generatedSourceFamilyReady() {
  const family = workspaceFamily("source");
  return family?.status === "ready" && Number(family.fileCount || 0) > 0;
}

function sourceBankFullSourceFile(bank, files) {
  const normalizedBank = String(bank || "").toLowerCase();
  const helperFile = `full-source/${normalizedBank}/bank_${normalizedBank}_helpers_asar.asm`;
  if (files.includes(helperFile)) {
    return helperFile;
  }
  return files.find((filePath) => filePath.startsWith(`full-source/${normalizedBank}/`) && /\.(asm|s)$/i.test(filePath)) || helperFile;
}

function sourceTreeFiles(files) {
  const priorityFiles = [
    "README.md",
    "bank-index.json",
    "full-source/c0/bank_c0_helpers_asar.asm",
    "full-source/c1/bank_c1_helpers_asar.asm",
    "full-source/c2/bank_c2_helpers_asar.asm"
  ].filter((filePath) => files.includes(filePath));
  const fullSourceFiles = files.filter((filePath) => filePath.startsWith("full-source/") && !priorityFiles.includes(filePath));
  const bankAnchorFiles = files.filter((filePath) => filePath.startsWith("banks/") && !priorityFiles.includes(filePath));
  const otherFiles = files.filter((filePath) => !priorityFiles.includes(filePath) && !fullSourceFiles.includes(filePath) && !bankAnchorFiles.includes(filePath));
  return [...priorityFiles, ...fullSourceFiles, ...otherFiles, ...bankAnchorFiles];
}

function renderLocalWorkspacePanel() {
  const rom = workspaceRom();
  const manifest = workspaceManifest();
  const electronAvailable = Boolean(window.earthboundWorkspace?.selectRom);
  const generatedCount = (manifest?.artifactFamilies || []).filter((family) => family.status === "ready").length;
  const status = rom
    ? rom.sha1Ok
      ? "Verified"
      : "Rejected"
    : "Notes-only";
  const statusClass = rom?.sha1Ok ? "ok" : rom ? "pending" : "";
  return `
    <section class="workspacePanel">
      <h2>Live Workspace Status</h2>
      ${state.workspaceMessage ? `<p class="workspaceNotice">${escapeHtml(state.workspaceMessage)}</p>` : ""}
      <div class="workspaceStatusGrid">
        <div class="workspaceStatusCard">
          <div class="workspaceStatusLabel">ROM</div>
          <div class="workspaceStatusValue">${rom ? escapeHtml(rom.fileName || rom.name || "Selected ROM") : "No ROM selected"}</div>
        </div>
        <div class="workspaceStatusCard">
          <div class="workspaceStatusLabel">Status</div>
          <div class="workspaceStatusValue"><span class="statusPill ${statusClass}">${escapeHtml(status)}</span></div>
        </div>
        <div class="workspaceStatusCard">
          <div class="workspaceStatusLabel">Headerless SHA-1</div>
          <div class="workspaceStatusValue">${rom?.headerlessSha1 ? escapeHtml(rom.headerlessSha1) : "Not available"}</div>
        </div>
        <div class="workspaceStatusCard">
          <div class="workspaceStatusLabel">Workspace</div>
          <div class="workspaceStatusValue">${manifest?.directories?.root ? escapeHtml(manifest.directories.root) : electronAvailable ? "Created after verified ROM selection" : "Electron app required for filesystem generation"}</div>
        </div>
      </div>
      <div class="workspaceActions">
        <button type="button" class="primaryAction" data-workspace-action="select-rom">${rom ? "Replace ROM" : "Add ROM"}</button>
        <button type="button" class="secondaryAction" data-entry-id="asset-library">Open Asset Library</button>
        <button type="button" class="secondaryAction" data-workspace-action="generate-all" ${manifest?.directories?.root && electronAvailable ? "" : "disabled"}>Generate all</button>
        <button type="button" class="secondaryAction" data-workspace-action="export-all" ${generatedCount && electronAvailable ? "" : "disabled"}>Export all zip</button>
        <button type="button" class="secondaryAction" data-workspace-action="open-workspace-folder" ${manifest?.directories?.root ? "" : "disabled"}>Open folder</button>
        <button type="button" class="secondaryAction" data-workspace-action="clear-workspace" ${rom ? "" : "disabled"}>Clear local state</button>
      </div>
      <p class="workspaceNotice">${electronAvailable ? "ROM selection creates an app-data workspace manifest. Generator stages will fill source, asset, audio, and export directories behind this same contract." : "This browser view can browse notes and contracts. Use the Electron app for filesystem workspace creation and generation."}</p>
    </section>
  `;
}

function renderGeneratedSourceTreePanel() {
  const files = sourceTreeFiles(workspaceFamilyFiles("source"));
  return `
    <section class="workspaceGeneratedPanel">
      <div class="workspaceGeneratedHeader">
        <h2>Generated Source Files</h2>
        <p>${generatedSourceFamilyReady() ? "Browse the complete decomp source copied into your local workspace, plus generated ROM-local bank anchors." : "Generate the Source Code family to browse local source files here."}</p>
      </div>
      ${renderGeneratedFileList("source", files, { limit: 80 })}
      <div class="workspaceActions">
        <button type="button" class="secondaryAction" data-workspace-action="generate-family" data-family-id="source" ${workspaceIsReady() && window.earthboundWorkspace?.generateFamily ? "" : "disabled"}>Generate source</button>
        <button type="button" class="secondaryAction" data-workspace-action="open-family-folder" data-family-id="source" ${files.length ? "" : "disabled"}>Open source folder</button>
      </div>
    </section>
  `;
}

function renderGeneratedSourceBankPanel(entry) {
  const bank = sourceBankFromEntry(entry);
  const files = workspaceFamilyFiles("source");
  const fullSourceFile = sourceBankFullSourceFile(bank, files);
  const bankAnchorFile = `banks/bank-${bank}.asm`;
  const fullSourceAvailable = files.includes(fullSourceFile);
  const bankAnchorAvailable = files.includes(bankAnchorFile);
  const fullSourcePreview = state.workspaceFilePreviews[workspacePreviewKey("source", fullSourceFile)];
  return `
    <section class="workspaceGeneratedPanel">
      <div class="workspaceGeneratedHeader">
        <h2>Generated Bank ${escapeHtml(bank.toUpperCase())} Source</h2>
        <p>${fullSourceAvailable ? "This page is hydrated from the complete decomp source copied into your local app-data workspace." : "Generate the Source Code family to hydrate this placeholder page with local source."}</p>
      </div>
      <div class="workspaceActions">
        <button type="button" class="primaryAction" data-workspace-file="true" data-family-id="source" data-file-path="${escapeHtml(fullSourceFile)}" ${fullSourceAvailable ? "" : "disabled"}>${fullSourcePreview?.content ? "Refresh full source" : "View full source"}</button>
        <button type="button" class="secondaryAction" data-workspace-file="true" data-family-id="source" data-file-path="${escapeHtml(bankAnchorFile)}" ${bankAnchorAvailable ? "" : "disabled"}>View bank anchor</button>
        <button type="button" class="secondaryAction" data-workspace-action="generate-family" data-family-id="source" ${workspaceIsReady() && window.earthboundWorkspace?.generateFamily ? "" : "disabled"}>Generate source</button>
        <button type="button" class="secondaryAction" data-workspace-action="open-family-folder" data-family-id="source" ${files.length ? "" : "disabled"}>Open source folder</button>
      </div>
      ${renderWorkspaceFilePreview("source", fullSourceFile)}
      ${renderWorkspaceFilePreview("source", bankAnchorFile)}
    </section>
  `;
}

function renderAssetLibraryPanel() {
  const contract = catalog.localWorkspaceContract || { artifactFamilies: [] };
  const manifest = workspaceManifest();
  const electronAvailable = Boolean(window.earthboundWorkspace?.generateFamily);
  const families = manifest?.artifactFamilies || contract.artifactFamilies || [];
  const generatedCount = families.filter((family) => family.status === "ready").length;
  return `
    <section class="assetLibraryPanel">
      <h2>Generated Artifact Families</h2>
      ${state.workspaceMessage ? `<p class="workspaceNotice">${escapeHtml(state.workspaceMessage)}</p>` : ""}
      <p class="workspaceNotice">These families are local-only. Generator and ZIP buttons require the Electron app, a verified ROM, and a local workspace manifest.</p>
      <div class="assetFamilyGrid">
        ${families.map((family) => renderAssetFamilyCard(family)).join("")}
      </div>
      ${families.some((family) => Array.isArray(family.files) && family.files.length) ? `
        <section class="generatedAssetBrowser">
          <h2>Generated Files</h2>
          ${families.map((family) => renderGeneratedFamilyBrowser(family)).join("")}
        </section>
      ` : ""}
      <div class="workspaceActions">
        <button type="button" class="primaryAction" data-workspace-action="select-rom">${workspaceIsReady() ? "Replace ROM" : "Add ROM"}</button>
        <button type="button" class="secondaryAction" data-workspace-action="generate-all" ${workspaceIsReady() && electronAvailable ? "" : "disabled"}>Generate all</button>
        <button type="button" class="secondaryAction" data-workspace-action="export-all" ${generatedCount && electronAvailable ? "" : "disabled"}>Export all zip</button>
        <button type="button" class="secondaryAction" data-entry-id="local-workspace">Local Workspace</button>
      </div>
    </section>
  `;
}

function renderGeneratedFamilyBrowser(family) {
  const files = Array.isArray(family.files) ? family.files : [];
  if (!files.length) {
    return "";
  }
  return `
    <section class="generatedFamilyBrowser">
      <div class="generatedFamilyHeader">
        <h3>${escapeHtml(family.label || family.id || "Generated Family")}</h3>
        <span>${files.length} file${files.length === 1 ? "" : "s"}</span>
      </div>
      ${renderGeneratedAssetSurface(family)}
      ${renderGeneratedFileList(family.id, files, { limit: 40 })}
    </section>
  `;
}

function renderGeneratedFileList(familyId, files, options = {}) {
  const visibleFiles = files.slice(0, options.limit || files.length);
  if (!visibleFiles.length) {
    return `<p class="workspaceNotice">No generated files are recorded for this family yet.</p>`;
  }
  return `
    <div class="generatedFileList">
      ${visibleFiles.map((filePath) => `
        <div class="generatedFileRow">
          <button type="button" class="generatedFileButton" data-workspace-file="true" data-family-id="${escapeHtml(familyId)}" data-file-path="${escapeHtml(filePath)}">${escapeHtml(filePath)}</button>
          ${renderWorkspaceFilePreview(familyId, filePath)}
        </div>
      `).join("")}
    </div>
    ${files.length > visibleFiles.length ? `<p class="workspaceNotice">Showing ${visibleFiles.length} of ${files.length} generated files.</p>` : ""}
  `;
}

function renderWorkspaceFilePreview(familyId, filePath) {
  const preview = state.workspaceFilePreviews[workspacePreviewKey(familyId, filePath)];
  if (!preview) {
    return "";
  }
  if (preview.error) {
    return `<p class="workspaceNotice">Could not preview ${escapeHtml(filePath)}: ${escapeHtml(preview.error)}</p>`;
  }
  const language = /\.json$/i.test(filePath) ? "json" : /\.(asm|s)$/i.test(filePath) ? "asm" : "";
  return `
    <div class="workspaceFilePreview">
      <div class="workspaceFileMeta">${escapeHtml(filePath)} - ${Number(preview.size || 0).toLocaleString("en-US")} bytes</div>
      ${renderCodeBlock(preview.content || "", language)}
    </div>
  `;
}

function filePreviewKind(filePath) {
  if (/\.(png|jpe?g|gif|webp)$/i.test(filePath)) {
    return "image";
  }
  if (/\.(wav|mp3|ogg|flac)$/i.test(filePath)) {
    return "audio";
  }
  return "text";
}

function prioritizeGeneratedMedia(files, familyId) {
  if (familyId === "graphics") {
    return [...files].sort((a, b) => {
      const aGroup = /overworld-sprites\/groups\//i.test(a);
      const bGroup = /overworld-sprites\/groups\//i.test(b);
      if (aGroup !== bGroup) {
        return aGroup ? -1 : 1;
      }
      const aSheet = /overworld-sprites\/sheets-preview\//i.test(a);
      const bSheet = /overworld-sprites\/sheets-preview\//i.test(b);
      if (aSheet !== bSheet) {
        return aSheet ? -1 : 1;
      }
      const aFrame = /frames/i.test(a) || /frames_2x3/i.test(a);
      const bFrame = /frames/i.test(b) || /frames_2x3/i.test(b);
      if (aFrame !== bFrame) {
        return aFrame ? -1 : 1;
      }
      return a.localeCompare(b);
    });
  }
  return [...files].sort((a, b) => a.localeCompare(b));
}

function renderGeneratedAssetSurface(family) {
  const files = Array.isArray(family.files) ? family.files : [];
  const imageFiles = prioritizeGeneratedMedia(files.filter((filePath) => filePreviewKind(filePath) === "image"), family.id);
  const audioFiles = prioritizeGeneratedMedia(files.filter((filePath) => filePreviewKind(filePath) === "audio"), family.id);
  if (family.id === "graphics") {
    return renderGraphicsFamilySurface(family, imageFiles);
  }
  if (family.id === "maps") {
    return renderMediaFamilySurface(family, imageFiles, "Map And Tileset Previews", "Generated map, tileset, palette, and collision preview images will appear here when those renderer stages emit them. The current first-stage generator records map handoff manifests.");
  }
  if (family.id === "audio") {
    return renderMediaFamilySurface(family, audioFiles, "Audio Playback", "Generated WAV previews will appear here after Music And Audio generation.");
  }
  return "";
}

function graphicsBankFromPath(filePath) {
  const match = String(filePath || "").match(/\/(d[1-5])\//i);
  return match ? match[1].toLowerCase() : "all";
}

function graphicsSpriteIdFromPath(filePath) {
  const match = String(filePath || "").match(/(?:sprite-)?(\d{4})/i);
  return match ? match[1] : "";
}

function graphicsMediaLabel(filePath) {
  const bank = graphicsBankFromPath(filePath);
  const spriteId = graphicsSpriteIdFromPath(filePath);
  if (/overworld-sprites\/groups\/all/i.test(filePath)) {
    return "All sprites contact sheet";
  }
  if (/overworld-sprites\/groups\/by-bank\//i.test(filePath)) {
    return `${bank.toUpperCase()} contact sheet`;
  }
  if (/overworld-sprites\/sheets-preview\//i.test(filePath)) {
    return `${bank.toUpperCase()} sprite ${spriteId || "sheet"}`;
  }
  if (/overworld-sprites\/frames\//i.test(filePath)) {
    return `${bank.toUpperCase()} sprite ${spriteId || "frame"} candidate frames`;
  }
  if (/tiles\//i.test(filePath)) {
    return `${bank.toUpperCase()} sprite ${spriteId || "tiles"} tile atlas`;
  }
  return filePath.split("/").pop() || filePath;
}

function renderGraphicsFamilySurface(family, imageFiles) {
  const groupFiles = imageFiles.filter((filePath) => /overworld-sprites\/groups\//i.test(filePath));
  const sheetFiles = imageFiles.filter((filePath) => /overworld-sprites\/sheets-preview\//i.test(filePath));
  const frameFiles = imageFiles.filter((filePath) => /overworld-sprites\/frames\//i.test(filePath));
  const tileFiles = imageFiles.filter((filePath) => /tiles\//i.test(filePath));
  const selectedBank = state.assetBrowser.graphicsBank || "all";
  const bankOptions = ["all", "d1", "d2", "d3", "d4", "d5"];
  const filteredSheets = selectedBank === "all"
    ? sheetFiles
    : sheetFiles.filter((filePath) => graphicsBankFromPath(filePath) === selectedBank);
  const visibleLimit = state.assetBrowser.graphicsShowAll ? filteredSheets.length : 120;
  const visibleSheets = filteredSheets.slice(0, visibleLimit);
  return `
    <section class="mediaFamilySurface graphicsBrowser">
      <div class="generatedFamilyHeader">
        <h3>Sprite And Graphics Browser</h3>
        <span>${sheetFiles.length ? `${sheetFiles.length} sprite sheet${sheetFiles.length === 1 ? "" : "s"}` : "renderer pending"}</span>
      </div>
      ${imageFiles.length ? `
        <div class="graphicsBrowserControls">
          <div class="segmentedControl" role="group" aria-label="Sprite bank filter">
            ${bankOptions.map((bank) => `
              <button type="button" class="${selectedBank === bank ? "active" : ""}" data-asset-browser-action="set-graphics-bank" data-bank="${escapeHtml(bank)}">${escapeHtml(bank === "all" ? "All" : bank.toUpperCase())}</button>
            `).join("")}
          </div>
          <button type="button" class="secondaryAction" data-asset-browser-action="toggle-graphics-show-all">${state.assetBrowser.graphicsShowAll ? "Show fewer sprites" : "Show all sprites"}</button>
          <button type="button" class="secondaryAction" data-asset-browser-action="load-visible-media" data-family-id="${escapeHtml(family.id)}">Load visible previews</button>
        </div>
        <div class="assetBrowserStats">
          ${groupFiles.length} grouped sheet${groupFiles.length === 1 ? "" : "s"} - ${filteredSheets.length} ${selectedBank === "all" ? "sprite sheets" : `${selectedBank.toUpperCase()} sprite sheets`} - ${frameFiles.length} candidate frame preview${frameFiles.length === 1 ? "" : "s"} - ${tileFiles.length} tile atlas preview${tileFiles.length === 1 ? "" : "s"}
        </div>
        ${groupFiles.length ? `
          <h4 class="mediaSubheading">Grouped Sheets</h4>
          <div class="mediaPreviewGrid groupedSheets">
            ${groupFiles.map((filePath) => renderMediaPreviewTile(family.id, filePath)).join("")}
          </div>
        ` : ""}
        ${visibleSheets.length ? `
          <h4 class="mediaSubheading">Individual Sprite Sheets</h4>
          <div class="mediaPreviewGrid spriteSheetGrid">
            ${visibleSheets.map((filePath) => renderMediaPreviewTile(family.id, filePath)).join("")}
          </div>
          ${filteredSheets.length > visibleSheets.length ? `<p class="workspaceNotice">Showing ${visibleSheets.length} of ${filteredSheets.length} sprite sheets. Use Show all sprites to expand this bank.</p>` : ""}
        ` : `<p class="workspaceNotice">No generated sprite sheets match this bank filter yet.</p>`}
      ` : `<p class="workspaceNotice">Generated sprite-sheet PNGs will appear here after Graphics And Sprites generation.</p>`}
    </section>
  `;
}

function renderMediaFamilySurface(family, mediaFiles, title, emptyMessage) {
  return `
    <section class="mediaFamilySurface">
      <div class="generatedFamilyHeader">
        <h3>${escapeHtml(title)}</h3>
        <span>${mediaFiles.length ? `${mediaFiles.length} preview file${mediaFiles.length === 1 ? "" : "s"}` : "renderer pending"}</span>
      </div>
      ${mediaFiles.length ? `
        <div class="mediaPreviewGrid">
          ${mediaFiles.slice(0, 24).map((filePath) => renderMediaPreviewTile(family.id, filePath)).join("")}
        </div>
      ` : `<p class="workspaceNotice">${escapeHtml(emptyMessage)}</p>`}
    </section>
  `;
}

function renderMediaPreviewTile(familyId, filePath) {
  const preview = state.workspaceMediaPreviews[workspacePreviewKey(familyId, filePath)];
  const kind = filePreviewKind(filePath);
  const audioSource = preview?.fileUrl || preview?.dataUrl || "";
  const label = familyId === "graphics" ? graphicsMediaLabel(filePath) : filePath;
  return `
    <div class="mediaPreviewTile">
      <button type="button" class="generatedFileButton" data-workspace-media="true" data-family-id="${escapeHtml(familyId)}" data-file-path="${escapeHtml(filePath)}" title="${escapeHtml(filePath)}">${escapeHtml(label)}</button>
      ${preview?.error ? `<p class="workspaceNotice">${escapeHtml(preview.error)}</p>` : ""}
      ${preview?.dataUrl && kind === "image" ? `<img src="${escapeHtml(preview.dataUrl)}" alt="${escapeHtml(filePath)}">` : ""}
      ${audioSource && kind === "audio" ? `
        <div class="audioPreviewMeta">${Number(preview.size || 0).toLocaleString("en-US")} bytes - local generated WAV</div>
        <audio controls preload="metadata" src="${escapeHtml(audioSource)}"></audio>
      ` : ""}
    </div>
  `;
}

function renderAssetFamilyCard(family) {
  const related = {
    source: "source-browser",
    graphics: "asset-contracts",
    maps: "chapter-map-scene-contracts",
    audio: "chapter-audio-pack-frontier",
    tables: "chapter-table-contracts"
  }[family.id] || "asset-contracts";
  const status = family.status || (workspaceIsReady() ? "pending-generator" : "needs-rom");
  const electronAvailable = Boolean(window.earthboundWorkspace?.generateFamily);
  const canGenerate = workspaceIsReady() && electronAvailable;
  const canExport = canGenerate && status === "ready" && Number(family.fileCount || 0) > 0;
  const fileMeta = Number(family.fileCount || 0)
    ? `${family.fileCount} generated file${Number(family.fileCount) === 1 ? "" : "s"}`
    : "No generated files yet";
  return `
    <article class="assetFamilyCard">
      <div class="assetFamilyLabel">${escapeHtml(family.id || "family")}</div>
      <div class="assetFamilyTitle">${escapeHtml(family.label || family.id || "Artifact Family")}</div>
      <p class="assetFamilySummary">${escapeHtml(family.summary || "Local generated artifacts.")}</p>
      <p><span class="statusPill ${status === "ready" ? "ok" : "pending"}">${escapeHtml(status)}</span> <span class="assetFamilyMeta">${escapeHtml(fileMeta)}</span></p>
      ${family.exportZip ? `<p class="workspaceNotice">Last ZIP: ${escapeHtml(family.exportZip)}</p>` : ""}
      <div class="assetFamilyActions">
        <button type="button" class="secondaryAction" data-entry-id="${escapeHtml(related)}">Contract</button>
        <button type="button" class="secondaryAction" data-workspace-action="generate-family" data-family-id="${escapeHtml(family.id || "")}" ${canGenerate ? "" : "disabled"}>Generate</button>
        <button type="button" class="secondaryAction" data-workspace-action="open-family-folder" data-family-id="${escapeHtml(family.id || "")}" ${canExport ? "" : "disabled"}>Open</button>
        <button type="button" class="secondaryAction" data-workspace-action="export-family" data-family-id="${escapeHtml(family.id || "")}" ${canExport ? "" : "disabled"}>Export zip</button>
      </div>
    </article>
  `;
}

async function handleWorkspaceAction(action, button = null) {
  if (action === "dismiss-first-run") {
    saveFirstRunDismissed(true);
    state.workspaceMessage = "Notes-only mode is active. You can add a ROM later from Local Workspace.";
    render();
    return;
  }
  if (action === "clear-workspace") {
    saveLocalWorkspaceState(null);
    state.workspaceMessage = "Local workspace state was cleared from this browser profile.";
    render();
    return;
  }
  if (action === "open-workspace-folder") {
    const folder = workspaceManifest()?.directories?.root;
    if (!folder || !window.earthboundWorkspace?.openFolder) {
      state.workspaceMessage = "Opening the workspace folder requires the Electron app and a verified ROM workspace.";
      render();
      return;
    }
    const result = await window.earthboundWorkspace.openFolder(folder);
    state.workspaceMessage = result?.ok ? "Opened local workspace folder." : `Could not open workspace folder: ${result?.error || "unknown error"}`;
    render();
    return;
  }
  if (action === "open-family-folder") {
    const family = workspaceFamily(button?.getAttribute("data-family-id"));
    const folder = family?.directory;
    if (!folder || !window.earthboundWorkspace?.openFolder) {
      state.workspaceMessage = "Opening a generated family folder requires the Electron app and generated family files.";
      render();
      return;
    }
    const result = await window.earthboundWorkspace.openFolder(folder);
    state.workspaceMessage = result?.ok ? `Opened ${family.label || family.id} folder.` : `Could not open family folder: ${result?.error || "unknown error"}`;
    render();
    return;
  }
  if (action === "generate-family") {
    await runWorkspaceJob("generate-family", button?.getAttribute("data-family-id"));
    return;
  }
  if (action === "generate-all") {
    await runWorkspaceJob("generate-all");
    return;
  }
  if (action === "export-family") {
    await runWorkspaceJob("export-family", button?.getAttribute("data-family-id"));
    return;
  }
  if (action === "export-all") {
    await runWorkspaceJob("export-all");
    return;
  }
  if (action === "select-rom") {
    await selectAndVerifyRom();
  }
}

function workspaceFamily(familyId) {
  return (workspaceManifest()?.artifactFamilies || []).find((family) => family.id === familyId) || null;
}

async function runWorkspaceJob(action, familyId = "") {
  const manifest = workspaceManifest();
  const workspaceRoot = manifest?.directories?.root;
  if (!workspaceRoot) {
    state.workspaceMessage = "Add and verify a ROM before running local generator stages.";
    render();
    return;
  }
  const api = window.earthboundWorkspace;
  if (!api) {
    state.workspaceMessage = "Generator and export jobs require the Electron app.";
    render();
    return;
  }
  const family = workspaceFamily(familyId);
  const familyLabel = family?.label || familyId || "workspace";
  state.workspaceMessage = action.includes("export")
    ? `Preparing ${familyId ? familyLabel : "all generated"} ZIP export...`
    : `Running ${familyId ? familyLabel : "all"} generator stage${familyId ? "" : "s"}...`;
  render();
  try {
    let result = null;
    if (action === "generate-family") {
      result = await api.generateFamily(workspaceRoot, familyId);
    } else if (action === "generate-all") {
      result = await api.generateAll(workspaceRoot);
    } else if (action === "export-family") {
      result = await api.exportFamily(workspaceRoot, familyId);
    } else if (action === "export-all") {
      result = await api.exportAll(workspaceRoot);
    }
    if (!result?.ok) {
      state.workspaceMessage = result?.error || "Workspace job failed.";
      render();
      return;
    }
    saveLocalWorkspaceState({
      ...state.localWorkspace,
      savedAt: new Date().toISOString(),
      manifest: result.manifest
    });
    if (result.zipPath) {
      state.workspaceMessage = `ZIP export created: ${result.zipPath}`;
    } else {
      state.workspaceMessage = familyId
        ? `${familyLabel} generator stage completed.`
        : "All generator stages completed.";
    }
    render();
  } catch (error) {
    state.workspaceMessage = `Workspace job failed: ${error?.message || error}`;
    render();
  }
}

async function handleAssetBrowserAction(button) {
  const action = button?.getAttribute("data-asset-browser-action") || "";
  if (action === "set-graphics-bank") {
    state.assetBrowser.graphicsBank = button?.getAttribute("data-bank") || "all";
    state.assetBrowser.graphicsShowAll = false;
    render();
    return;
  }
  if (action === "toggle-graphics-show-all") {
    state.assetBrowser.graphicsShowAll = !state.assetBrowser.graphicsShowAll;
    render();
    return;
  }
  if (action === "load-visible-media") {
    await loadVisibleMediaPreviews(button?.getAttribute("data-family-id") || "");
  }
}

async function loadVisibleMediaPreviews(familyId) {
  const manifest = workspaceManifest();
  const workspaceRoot = manifest?.directories?.root;
  if (!workspaceRoot || !familyId || !window.earthboundWorkspace?.readMedia) {
    state.workspaceMessage = "Media previews require the Electron app and a generated workspace.";
    render();
    return;
  }
  const buttons = [...documentEl.querySelectorAll(`[data-workspace-media="true"][data-family-id="${CSS.escape(familyId)}"]`)];
  const filePaths = buttons
    .map((button) => button.getAttribute("data-file-path") || "")
    .filter(Boolean)
    .filter((filePath, index, list) => list.indexOf(filePath) === index)
    .filter((filePath) => !state.workspaceMediaPreviews[workspacePreviewKey(familyId, filePath)]?.dataUrl && !state.workspaceMediaPreviews[workspacePreviewKey(familyId, filePath)]?.fileUrl);
  if (!filePaths.length) {
    state.workspaceMessage = "Visible previews are already loaded.";
    render();
    return;
  }
  state.workspaceMessage = `Loading ${filePaths.length} visible preview${filePaths.length === 1 ? "" : "s"}...`;
  render();
  for (const filePath of filePaths) {
    const key = workspacePreviewKey(familyId, filePath);
    try {
      const result = await window.earthboundWorkspace.readMedia(workspaceRoot, familyId, filePath);
      state.workspaceMediaPreviews[key] = result?.ok
        ? result.media
        : { error: result?.error || "Could not read generated media." };
    } catch (error) {
      state.workspaceMediaPreviews[key] = { error: error?.message || String(error) };
    }
  }
  state.workspaceMessage = `Loaded ${filePaths.length} visible preview${filePaths.length === 1 ? "" : "s"}.`;
  render();
}

async function loadWorkspaceFilePreview(button) {
  const manifest = workspaceManifest();
  const workspaceRoot = manifest?.directories?.root;
  const familyId = button?.getAttribute("data-family-id") || "";
  const filePath = button?.getAttribute("data-file-path") || "";
  const key = workspacePreviewKey(familyId, filePath);
  if (!workspaceRoot || !familyId || !filePath || !window.earthboundWorkspace?.readFile) {
    state.workspaceFilePreviews[key] = { error: "File previews require the Electron app and a generated workspace." };
    render();
    return;
  }
  state.workspaceMessage = `Loading ${filePath}...`;
  render();
  try {
    const result = await window.earthboundWorkspace.readFile(workspaceRoot, familyId, filePath);
    if (!result?.ok) {
      state.workspaceFilePreviews[key] = { error: result?.error || "Could not read generated file." };
      state.workspaceMessage = state.workspaceFilePreviews[key].error;
      render();
      return;
    }
    state.workspaceFilePreviews[key] = result.file;
    state.workspaceMessage = `Loaded ${filePath}.`;
    render();
  } catch (error) {
    state.workspaceFilePreviews[key] = { error: error?.message || String(error) };
    state.workspaceMessage = `Could not load ${filePath}.`;
    render();
  }
}

async function loadWorkspaceMediaPreview(button) {
  const manifest = workspaceManifest();
  const workspaceRoot = manifest?.directories?.root;
  const familyId = button?.getAttribute("data-family-id") || "";
  const filePath = button?.getAttribute("data-file-path") || "";
  const key = workspacePreviewKey(familyId, filePath);
  if (!workspaceRoot || !familyId || !filePath || !window.earthboundWorkspace?.readMedia) {
    state.workspaceMediaPreviews[key] = { error: "Media previews require the Electron app and a generated workspace." };
    render();
    return;
  }
  state.workspaceMessage = `Loading ${filePath}...`;
  render();
  try {
    const result = await window.earthboundWorkspace.readMedia(workspaceRoot, familyId, filePath);
    if (!result?.ok) {
      state.workspaceMediaPreviews[key] = { error: result?.error || "Could not read generated media." };
      state.workspaceMessage = state.workspaceMediaPreviews[key].error;
      render();
      return;
    }
    state.workspaceMediaPreviews[key] = result.media;
    state.workspaceMessage = `Loaded ${filePath}.`;
    render();
  } catch (error) {
    state.workspaceMediaPreviews[key] = { error: error?.message || String(error) };
    state.workspaceMessage = `Could not load ${filePath}.`;
    render();
  }
}

async function selectAndVerifyRom() {
  state.workspaceMessage = "Waiting for ROM selection...";
  render();
  try {
    if (window.earthboundWorkspace?.selectRom) {
      const result = await window.earthboundWorkspace.selectRom();
      if (result?.canceled) {
        state.workspaceMessage = "ROM selection canceled.";
      } else if (result?.rom?.sha1Ok) {
        saveLocalWorkspaceState({
          mode: "electron",
          savedAt: new Date().toISOString(),
          rom: result.rom,
          manifest: result.manifest
        });
        saveFirstRunDismissed(true);
        state.workspaceMessage = "ROM verified. Local source, asset, table, map, and audio indexes generated.";
        if (entries.has("asset-library")) {
          openEntry("asset-library", { pushHistory: false });
          return;
        }
      } else {
        saveLocalWorkspaceState({
          mode: "electron",
          savedAt: new Date().toISOString(),
          rom: result?.rom || null,
          manifest: null
        });
        state.workspaceMessage = "ROM did not match the expected EarthBound US headerless SHA-1.";
      }
      render();
      return;
    }
    const browserResult = await selectRomInBrowser();
    if (!browserResult) {
      state.workspaceMessage = "ROM selection canceled.";
    } else if (browserResult.rom.sha1Ok) {
      saveLocalWorkspaceState({
        mode: "browser-verified",
        savedAt: new Date().toISOString(),
        rom: browserResult.rom,
        manifest: null
      });
      saveFirstRunDismissed(true);
      state.workspaceMessage = "ROM identity verified in browser mode. Use Electron for filesystem generation.";
    } else {
      saveLocalWorkspaceState({
        mode: "browser-verified",
        savedAt: new Date().toISOString(),
        rom: browserResult.rom,
        manifest: null
      });
      state.workspaceMessage = "ROM did not match the expected EarthBound US headerless SHA-1.";
    }
    render();
  } catch (error) {
    state.workspaceMessage = `ROM verification failed: ${error?.message || error}`;
    render();
  }
}

function selectRomInBrowser() {
  return new Promise((resolve, reject) => {
    const input = document.createElement("input");
    input.type = "file";
    input.accept = ".sfc,.smc";
    input.addEventListener("change", async () => {
      const file = input.files?.[0];
      if (!file) {
        resolve(null);
        return;
      }
      try {
        resolve({ rom: await verifyBrowserRom(file) });
      } catch (error) {
        reject(error);
      }
    }, { once: true });
    input.click();
  });
}

async function verifyBrowserRom(file) {
  const contract = catalog.localWorkspaceContract || {};
  const expected = contract.expectedRom || {};
  const headerlessSize = Number(expected.headerlessSize || 3145728);
  const headeredSize = Number(expected.headeredSize || headerlessSize + 512);
  const expectedSha1 = String(expected.headerlessSha1 || "").toLowerCase();
  const buffer = await file.arrayBuffer();
  const bytes = new Uint8Array(buffer);
  const headered = bytes.byteLength === headeredSize;
  const headerless = bytes.byteLength === headerlessSize;
  const payload = headered ? bytes.slice(512) : bytes;
  const headerlessSha1 = await sha1Hex(payload);
  const fileSha1 = await sha1Hex(bytes);
  return {
    fileName: file.name,
    size: bytes.byteLength,
    headered,
    headerless,
    sizeOk: headered || headerless,
    fileSha1,
    headerlessSha1,
    sha1Ok: headerlessSha1 === expectedSha1,
    expectedHeaderlessSha1: expectedSha1,
    expectedHeaderlessSize: headerlessSize,
    expectedHeaderedSize: headeredSize,
    verifiedAt: new Date().toISOString()
  };
}

async function sha1Hex(bytes) {
  const digest = await window.crypto.subtle.digest("SHA-1", bytes);
  return [...new Uint8Array(digest)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

function renderTopicHub() {
  const headingCounts = new Map();
  const topicSectionId = registerHubSection("Topic Areas", headingCounts);
  const supportingSectionId = registerHubSection("Supporting Indexes", headingCounts);
  const topics = catalog.entries
    .filter((entry) => entry.kind === "topic" && entry.id !== "topic-index")
    .sort((a, b) => (a.tocPriority ?? 50) - (b.tocPriority ?? 50) || (b.noteRefs?.length || 0) - (a.noteRefs?.length || 0) || a.title.localeCompare(b.title));
  const supportIds = ["narrative-index", "learning-path-index", "relationship-graph", "bank-map", "source-browser", "asset-manifest-index"];
  return `
    <section class="hubPage">
      <section class="hubSection" id="${escapeHtml(topicSectionId)}">
        <div class="hubSectionHeader">
          <h2>Topic Areas</h2>
          <p>Generated evidence clusters that sit between the polished chapters and the raw note archive.</p>
        </div>
        <div class="hubGrid">
          ${topics.map((entry) => renderHubCard(entry, {
            eyebrow: `${entry.noteRefs?.length || 0} evidence notes`,
            meta: evidenceMeta(entry),
            tags: entry.banks?.map((bank) => `Bank ${bank}`).slice(0, 5) || []
          })).join("")}
        </div>
      </section>
      <section class="hubSection" id="${escapeHtml(supportingSectionId)}">
        <div class="hubSectionHeader">
          <h2>Supporting Indexes</h2>
          <p>Navigation surfaces for switching from topic-level reading into banks, source, assets, and graph exploration.</p>
        </div>
        <div class="hubGrid compact">
          ${supportIds.filter((id) => entries.has(id)).map((id) => renderHubCard(entries.get(id), {
            eyebrow: entries.get(id).kind,
            meta: evidenceMeta(entries.get(id))
          })).join("")}
        </div>
      </section>
    </section>
  `;
}

function renderSourceBrowserHub() {
  const headingCounts = new Map();
  const bankSectionId = registerHubSection("Source Banks", headingCounts);
  const indexSectionId = registerHubSection("Source Indexes", headingCounts);
  const sourceBanks = catalog.entries
    .filter((entry) => /^source-bank-[c-e][0-9a-f]$/i.test(entry.id))
    .sort((a, b) => (a.banks?.[0] || "").localeCompare(b.banks?.[0] || ""));
  const indexIds = ["source-tree", "routine-index", "bank-map", "relationship-graph", "workflows"];
  return `
    <section class="hubPage">
      <section class="hubSection" id="${escapeHtml(bankSectionId)}">
        <div class="hubSectionHeader">
          <h2>Source Banks</h2>
          <p>Bank-level entry points into checked-in source files, routine pages, and scaffold/data files.</p>
        </div>
        <div class="sourceBankGrid">
          ${sourceBanks.map((entry) => renderSourceBankCard(entry)).join("")}
        </div>
      </section>
      <section class="hubSection" id="${escapeHtml(indexSectionId)}">
        <div class="hubSectionHeader">
          <h2>Source Indexes</h2>
          <p>Higher-level maps for moving from source files into routines, workflows, validation, and relationships.</p>
        </div>
        <div class="hubGrid compact">
          ${indexIds.filter((id) => entries.has(id)).map((id) => renderHubCard(entries.get(id), {
            eyebrow: entries.get(id).kind,
            meta: evidenceMeta(entries.get(id))
          })).join("")}
        </div>
      </section>
    </section>
  `;
}

function registerHubSection(title, counts) {
  const sectionId = uniqueHeadingId(title, counts);
  currentDocumentOutline.push({ id: sectionId, level: 2, title });
  return sectionId;
}

function renderHubCard(entry, options = {}) {
  if (!entry) {
    return "";
  }
  const tags = options.tags || [
    ...(entry.banks || []).map((bank) => `Bank ${bank}`),
    ...(entry.addresses || []).slice(0, 2)
  ];
  const secondary = options.secondaryId && entries.has(options.secondaryId)
    ? `<button type="button" class="hubCardAction secondary" data-entry-id="${escapeHtml(options.secondaryId)}">${escapeHtml(options.secondaryLabel || entries.get(options.secondaryId).title)}</button>`
    : "";
  return `
    <article class="hubCard">
      <div class="hubCardEyebrow">${escapeHtml(options.eyebrow || entry.kind)}</div>
      <h3>${escapeHtml(entry.title)}</h3>
      ${entry.summary ? `<p>${escapeHtml(entry.summary)}</p>` : ""}
      ${options.meta ? `<div class="hubCardMeta">${escapeHtml(options.meta)}</div>` : ""}
      ${tags.length ? `<div class="referenceTags">${tags.slice(0, 5).map((tag) => `<span>${escapeHtml(tag)}</span>`).join("")}</div>` : ""}
      <div class="hubCardActions">
        <button type="button" class="hubCardAction" data-entry-id="${escapeHtml(entry.id)}">Open</button>
        ${secondary}
      </div>
    </article>
  `;
}

function renderSourceBankCard(entry) {
  const bank = entry.banks?.[0] || entry.title.replace(/^Bank\s+/i, "").replace(/\s+.*/, "");
  const fileCount = sourceFileCount(entry.summary);
  const routineIndexId = `routine-index-${String(bank).toLowerCase()}`;
  const bankEntryId = `bank-${String(bank).toLowerCase()}`;
  return `
    <article class="sourceBankCard">
      <div>
        <div class="sourceBankCode">${escapeHtml(bank)}</div>
        <h3>${escapeHtml(entry.title)}</h3>
        ${entry.summary ? `<p>${escapeHtml(entry.summary)}</p>` : ""}
      </div>
      <div class="sourceBankStats">
        ${fileCount ? `<span>${escapeHtml(fileCount)} files</span>` : ""}
        ${entries.has(routineIndexId) ? `<span>routine index</span>` : ""}
      </div>
      <div class="hubCardActions">
        <button type="button" class="hubCardAction" data-entry-id="${escapeHtml(entry.id)}">Source files</button>
        ${entries.has(bankEntryId) ? `<button type="button" class="hubCardAction secondary" data-entry-id="${escapeHtml(bankEntryId)}">Bank page</button>` : ""}
        ${entries.has(routineIndexId) ? `<button type="button" class="hubCardAction secondary" data-entry-id="${escapeHtml(routineIndexId)}">Routines</button>` : ""}
      </div>
    </article>
  `;
}

function learningPathForChapter(entry) {
  const inferred = entry.id.replace(/^chapter-/, "learning-");
  if (entries.has(inferred)) {
    return inferred;
  }
  return (entry.related || []).find((id) => entries.get(id)?.kind === "learning-path") || "";
}

function learningPathMeta(entry) {
  const steps = entry.learningPath?.steps || [];
  const links = steps.reduce((total, step) => total + (step.items?.length || 0), 0);
  return `${steps.length} stages - ${links} linked references`;
}

function evidenceMeta(entry) {
  const parts = [];
  if (entry.noteRefs?.length) {
    parts.push(`${entry.noteRefs.length} note ref${entry.noteRefs.length === 1 ? "" : "s"}`);
  }
  if (entry.sourceRefs?.length) {
    parts.push(`${entry.sourceRefs.length} source ref${entry.sourceRefs.length === 1 ? "" : "s"}`);
  }
  if (entry.related?.length) {
    parts.push(`${entry.related.length} related`);
  }
  return parts.join(" - ");
}

function sourceFileCount(summary) {
  const match = String(summary || "").match(/for\s+([\d,]+)\s+checked-in/i);
  return match ? match[1] : "";
}

function renderLearningPathIndex() {
  const headingCounts = new Map();
  const sectionId = uniqueHeadingId("Guided Routes", headingCounts);
  currentDocumentOutline.push({ id: sectionId, level: 2, title: "Guided Routes" });
  const paths = catalog.entries
    .filter((entry) => entry.kind === "learning-path" && entry.id !== "learning-path-index" && entry.learningPath)
    .sort((a, b) => {
      const priority = (a.tocPriority ?? 50) - (b.tocPriority ?? 50);
      return priority || a.title.localeCompare(b.title);
    });
  return `
    <section class="learningPathGuide">
      <section class="learningStep" id="${escapeHtml(sectionId)}">
        <div class="learningStepMarker">1</div>
        <div class="learningStepBody">
          <h2>Guided Routes</h2>
          <p>Each path starts with a curated chapter, then branches into primary notes, source references, topic pages, and search vocabulary.</p>
          <div class="learningCardGrid">
            ${paths.map((entry) => {
              const path = entry.learningPath || {};
              const stepCount = path.steps?.length || 0;
              const linkCount = (path.steps || []).reduce((total, step) => total + (step.items?.length || 0), 0);
              return `
                <button type="button" class="learningCard" data-entry-id="${escapeHtml(entry.id)}">
                  <span class="learningCardTitle">${escapeHtml(entry.title)}</span>
                  <span class="learningCardMeta">${stepCount} stages - ${linkCount} linked references</span>
                  ${entry.summary ? `<span class="learningCardSummary">${escapeHtml(entry.summary)}</span>` : ""}
                  ${entry.banks?.length ? `<span class="referenceTags">${entry.banks.slice(0, 4).map((bank) => `<span>Bank ${escapeHtml(bank)}</span>`).join("")}</span>` : ""}
                </button>
              `;
            }).join("")}
          </div>
        </div>
      </section>
    </section>
  `;
}

function renderLearningPathGuide(entry) {
  const path = entry.learningPath || {};
  const headingCounts = new Map();
  const steps = (path.steps || []).map((step, index) => {
    const title = step.title || `Step ${index + 1}`;
    const sectionId = uniqueHeadingId(title, headingCounts);
    currentDocumentOutline.push({ id: sectionId, level: 2, title });
    return `
      <section class="learningStep" id="${escapeHtml(sectionId)}">
        <div class="learningStepMarker">${index + 1}</div>
        <div class="learningStepBody">
          <h2>${escapeHtml(title)}</h2>
          ${step.summary ? `<p>${escapeHtml(step.summary)}</p>` : ""}
          ${renderLearningConcepts(step.concepts || [])}
          ${renderLearningItems(step.items || [])}
          ${renderLearningTerms(step.terms || [])}
        </div>
      </section>
    `;
  }).join("");
  if (path.promotionNote) {
    const promotionId = uniqueHeadingId("Promotion Note", headingCounts);
    currentDocumentOutline.push({ id: promotionId, level: 2, title: "Promotion Note" });
    return `
      <section class="learningPathGuide">
        ${steps}
        <section class="learningStep learningStepNote" id="${escapeHtml(promotionId)}">
          <div class="learningStepMarker">!</div>
          <div class="learningStepBody">
            <h2>Promotion Note</h2>
            <p>${escapeHtml(path.promotionNote)}</p>
          </div>
        </section>
      </section>
    `;
  }
  return `<section class="learningPathGuide">${steps}</section>`;
}

function renderLearningConcepts(concepts) {
  if (!concepts.length) {
    return "";
  }
  return `
    <div class="learningConceptGrid">
      ${concepts.map((concept) => `
        <div class="learningConcept">
          <span>${escapeHtml(concept.title || "Concept")}</span>
          ${concept.summary ? `<small>${escapeHtml(concept.summary)}</small>` : ""}
        </div>
      `).join("")}
    </div>
  `;
}

function renderLearningItems(items) {
  const validItems = items.filter((item) => item && item.id && entries.has(item.id));
  if (!validItems.length) {
    return "";
  }
  return `
    <div class="learningCardGrid">
      ${validItems.map((item) => `
        <button type="button" class="learningCard" data-entry-id="${escapeHtml(item.id)}">
          <span class="learningCardTitle">${escapeHtml(item.title || item.id)}</span>
          ${item.meta ? `<span class="learningCardMeta">${escapeHtml(item.meta)}</span>` : ""}
          ${item.summary ? `<span class="learningCardSummary">${escapeHtml(item.summary)}</span>` : ""}
          ${item.tags?.length ? `<span class="referenceTags">${item.tags.slice(0, 4).map((tag) => `<span>${escapeHtml(tag)}</span>`).join("")}</span>` : ""}
        </button>
      `).join("")}
    </div>
  `;
}

function renderLearningTerms(terms) {
  if (!terms.length) {
    return "";
  }
  return `<div class="learningTerms">${terms.map((term) => `<code>${escapeHtml(term)}</code>`).join("")}</div>`;
}

function renderReferenceWorkbench(entry) {
  if (!shouldShowReferenceWorkbench(entry)) {
    return "";
  }
  const sections = [];
  const chapterEvidence = (entry.chapterEvidence || []).filter((item) => item.id && entries.has(item.id));
  if (chapterEvidence.length) {
    sections.push(referenceSection("Chapter Evidence", chapterEvidence.slice(0, 12).map((item) => referenceCard({
      id: item.id,
      title: item.title,
      meta: [
        item.configured ? "Primary note" : "Related note",
        item.bank ? `Bank ${item.bank}` : "",
        item.length ? `${Number(item.length).toLocaleString("en-US")} chars` : ""
      ].filter(Boolean).join(" - "),
      summary: item.summary,
      tags: [
        ...(item.topics || []).map((topicId) => entries.get(topicId)?.title || topicId).slice(0, 3),
        ...(item.headings || []).slice(0, 2)
      ]
    }))));
  }

  const noteCards = (entry.noteRefs || [])
    .filter((ref) => ref.entryId && entries.has(ref.entryId) && !chapterEvidence.some((item) => item.id === ref.entryId))
    .slice(0, 10)
    .map((ref) => {
      const noteEntry = entries.get(ref.entryId);
      return referenceCard({
        id: ref.entryId,
        title: noteEntry.title,
        meta: "Evidence note",
        summary: noteEntry.summary || ref.path,
        tags: [ref.path]
      });
    });
  if (noteCards.length) {
    sections.push(referenceSection("Additional Notes", noteCards));
  }

  const sourceCards = (entry.sourceRefs || [])
    .filter((ref) => ref.entryId && entries.has(ref.entryId))
    .slice(0, 10)
    .map((ref) => {
      const sourceEntry = entries.get(ref.entryId);
      return referenceCard({
        id: ref.entryId,
        title: sourceEntry.title,
        meta: sourceEntry.kind,
        summary: sourceEntry.summary || ref.path,
        tags: [ref.path]
      });
    });
  if (sourceCards.length) {
    sections.push(referenceSection("Source References", sourceCards));
  }

  const relatedCards = (entry.related || [])
    .filter((id) => entries.has(id))
    .slice(0, 10)
    .map((id) => {
      const related = entries.get(id);
      return referenceCard({
        id,
        title: related.title,
        meta: related.kind,
        summary: related.summary,
        tags: related.banks?.map((bank) => `Bank ${bank}`).slice(0, 3) || []
      });
    });
  if (relatedCards.length) {
    sections.push(referenceSection("Related Reading", relatedCards));
  }

  const bankCards = (entry.banks || [])
    .map((bank) => `bank-${bank.toLowerCase()}`)
    .filter((id) => entries.has(id))
    .slice(0, 8)
    .map((id) => {
      const bankEntry = entries.get(id);
      return referenceCard({
        id,
        title: bankEntry.title,
        meta: "Bank",
        summary: bankEntry.summary,
        tags: bankEntry.addresses?.slice(0, 2) || []
      });
    });
  if (bankCards.length) {
    sections.push(referenceSection("Bank Context", bankCards));
  }

  const inboundCards = directedGraphNeighbors(entry.id, "in", 12)
    .filter((neighbor) => {
      const neighborEntry = entries.get(neighbor.id);
      return neighborEntry && neighborEntry.kind !== "search";
    })
    .map((neighbor) => {
      const inboundEntry = entries.get(neighbor.id);
      return referenceCard({
        id: neighbor.id,
        title: inboundEntry.title,
        meta: edgeLabel(neighbor),
        summary: inboundEntry.summary,
        tags: [
          inboundEntry.kind,
          ...(inboundEntry.banks || []).map((bank) => `Bank ${bank}`)
        ]
      });
    });
  if (inboundCards.length) {
    sections.push(referenceSection("Referenced By", inboundCards));
  }

  if (!sections.length) {
    return "";
  }
  return `
    <section class="referenceWorkbench">
      <div class="referenceHeader">
        <h2>Reference Shelf</h2>
        <p>Generated links for moving from the explanation to the underlying evidence.</p>
      </div>
      ${sections.join("")}
    </section>
  `;
}

function shouldShowReferenceWorkbench(entry) {
  if (entry.id === "relationship-graph" || entry.kind === "search") {
    return false;
  }
  if (["note", "source", "source-file", "routine", "symbol", "asset", "tool"].includes(entry.kind)) {
    return directedGraphNeighbors(entry.id, "in", 1).length > 0;
  }
  return Boolean(
    (entry.chapterEvidence && entry.chapterEvidence.length)
    || (entry.noteRefs && entry.noteRefs.some((ref) => ref.entryId && entries.has(ref.entryId)))
    || (entry.sourceRefs && entry.sourceRefs.some((ref) => ref.entryId && entries.has(ref.entryId)))
    || (entry.related && entry.related.some((id) => entries.has(id)))
    || (entry.banks && entry.banks.some((bank) => entries.has(`bank-${bank.toLowerCase()}`)))
    || directedGraphNeighbors(entry.id, "in", 1).length > 0
  );
}

function referenceSection(title, cards) {
  if (!cards.length) {
    return "";
  }
  return `
    <section class="referenceSection">
      <h3>${escapeHtml(title)}</h3>
      <div class="referenceGrid">${cards.join("")}</div>
    </section>
  `;
}

function referenceCard({ id, title, meta, summary, tags = [] }) {
  return `
    <button type="button" class="referenceCard" data-entry-id="${escapeHtml(id)}">
      <span class="referenceCardTitle">${escapeHtml(title || id)}</span>
      ${meta ? `<span class="referenceCardMeta">${escapeHtml(meta)}</span>` : ""}
      ${summary ? `<span class="referenceCardSummary">${escapeHtml(summary)}</span>` : ""}
      ${tags.length ? `<span class="referenceTags">${tags.slice(0, 5).map((tag) => `<span>${escapeHtml(tag)}</span>`).join("")}</span>` : ""}
    </button>
  `;
}

function renderRelationshipGraphDocument() {
  const focusId = entries.has(state.graphFocusId) ? state.graphFocusId : "overview";
  const focusEntry = entries.get(focusId) || entries.get("overview");
  const hubs = (relationshipGraph.topHubs || []).filter((id) => entries.has(id));
  const stats = relationshipGraph.stats || {};
  return `
    <section class="graphWorkbench">
      <div class="graphHeader">
        <div>
          <div class="graphEyebrow">Graph Focus</div>
          <h2>${escapeHtml(focusEntry.title)}</h2>
          <p>${escapeHtml(focusEntry.summary || "Connected encyclopedia entry.")}</p>
        </div>
        <div class="graphStats">
          <span>${Number(stats.nodeCount || 0).toLocaleString("en-US")} nodes</span>
          <span>${Number(stats.edgeCount || 0).toLocaleString("en-US")} edges</span>
          <span>${Number(stats.linkedNodeCount || 0).toLocaleString("en-US")} linked</span>
        </div>
      </div>
      ${renderGraphNeighborhood(focusId, { large: true })}
      <div class="graphHubPanel">
        <h3>High-Traffic Hubs</h3>
        <div class="graphHubList">
          ${hubs.map((id) => {
            const entry = entries.get(id);
            const node = graphNodes.get(id);
            return `<button type="button" class="graphHubButton" data-graph-focus-id="${escapeHtml(id)}">
              <span>${escapeHtml(entry.title)}</span>
              <small>${escapeHtml(entry.kind)} - ${Number(node?.degree || 0).toLocaleString("en-US")} links</small>
            </button>`;
          }).join("")}
        </div>
      </div>
    </section>
  `;
}

function renderEntryGraphPreview(entry) {
  if (entry.id === "search-results") {
    return "";
  }
  const neighbors = graphNeighbors(entry.id, 10);
  if (!neighbors.length) {
    return "";
  }
  return `
    <section class="entryGraphPreview">
      <div class="entryGraphTitle">
        <div>
          <h2>Relationship Graph</h2>
          <p>Closest generated links for this entry.</p>
        </div>
        <button type="button" class="loadBodyButton" data-open-graph-focus-id="${escapeHtml(entry.id)}">Open graph</button>
      </div>
      ${renderGraphNeighborhood(entry.id, { limit: 10, compact: true })}
    </section>
  `;
}

function renderGraphNeighborhood(centerId, options = {}) {
  const centerEntry = entries.get(centerId);
  if (!centerEntry) {
    return "";
  }
  const limit = options.limit || (options.large ? 18 : 12);
  const neighbors = graphNeighbors(centerId, limit);
  if (!neighbors.length) {
    return `<div class="graphEmpty">No generated relationships for this entry yet.</div>`;
  }
  return `
    <div class="graphNeighborhood${options.large ? " large" : ""}${options.compact ? " compact" : ""}">
      ${renderGraphSvg(centerId, neighbors, options)}
      <div class="graphNeighborList">
        ${neighbors.map((neighbor) => {
          const entry = entries.get(neighbor.id);
          return `<button type="button" class="graphNeighbor" data-entry-id="${escapeHtml(neighbor.id)}">
            <span>${escapeHtml(entry.title)}</span>
            <small>${escapeHtml(edgeLabel(neighbor))}</small>
          </button>`;
        }).join("")}
      </div>
    </div>
  `;
}

function graphNeighbors(id, limit = 18) {
  return ((relationshipGraph.neighborhoods || {})[id] || [])
    .filter((neighbor) => entries.has(neighbor.id))
    .slice(0, limit);
}

function directedGraphNeighbors(id, direction, limit = 18) {
  return ((relationshipGraph.neighborhoods || {})[id] || [])
    .filter((neighbor) => entries.has(neighbor.id) && (neighbor.directions || []).includes(direction))
    .slice(0, limit);
}

function renderGraphSvg(centerId, neighbors, options = {}) {
  const centerEntry = entries.get(centerId);
  const width = options.large ? 760 : 620;
  const height = options.large ? 420 : 300;
  const cx = width / 2;
  const cy = height / 2;
  const radius = options.large ? 155 : 105;
  const nodes = neighbors.map((neighbor, index) => {
    const angle = -Math.PI / 2 + (index / neighbors.length) * Math.PI * 2;
    return {
      ...neighbor,
      x: cx + Math.cos(angle) * radius,
      y: cy + Math.sin(angle) * radius,
      entry: entries.get(neighbor.id)
    };
  });
  return `
    <svg class="graphSvg" viewBox="0 0 ${width} ${height}" role="img" aria-label="Relationship graph centered on ${escapeHtml(centerEntry.title)}">
      <g class="graphEdges">
        ${nodes.map((node) => `<line x1="${cx}" y1="${cy}" x2="${node.x.toFixed(1)}" y2="${node.y.toFixed(1)}"></line>`).join("")}
      </g>
      <g class="graphCenter" data-entry-id="${escapeHtml(centerId)}">
        <circle cx="${cx}" cy="${cy}" r="${options.large ? 38 : 30}"></circle>
        <text x="${cx}" y="${cy - 3}" text-anchor="middle">${escapeHtml(shortGraphLabel(centerEntry.title, 18))}</text>
        <text x="${cx}" y="${cy + 13}" text-anchor="middle" class="graphKindLabel">${escapeHtml(centerEntry.kind)}</text>
      </g>
      ${nodes.map((node) => `
        <g class="graphNode graphNode-${escapeHtml(node.entry.kind)}" data-entry-id="${escapeHtml(node.id)}">
          <circle cx="${node.x.toFixed(1)}" cy="${node.y.toFixed(1)}" r="${nodeRadius(node)}"></circle>
          <text x="${node.x.toFixed(1)}" y="${(node.y + nodeRadius(node) + 14).toFixed(1)}" text-anchor="middle">${escapeHtml(shortGraphLabel(node.entry.title, 16))}</text>
        </g>
      `).join("")}
    </svg>
  `;
}

function nodeRadius(node) {
  return Math.max(11, Math.min(24, 10 + Math.sqrt(node.weight || 1) * 2));
}

function shortGraphLabel(value, maxLength) {
  const text = String(value || "");
  return text.length > maxLength ? `${text.slice(0, maxLength - 1)}...` : text;
}

function edgeLabel(neighbor) {
  const types = (neighbor.types || []).join(", ");
  const directions = (neighbor.directions || []).includes("in") && (neighbor.directions || []).includes("out")
    ? "mutual"
    : (neighbor.directions || [])[0] === "in"
      ? "links here"
      : "links out";
  return `${types || "related"} - ${directions}`;
}

function buildReferenceIndex() {
  const index = new Map();
  const weights = new Map();

  function register(value, entry, weight = 1) {
    for (const key of referenceKeys(value)) {
      if (!isUsefulReferenceKey(key)) {
        continue;
      }
      const existingWeight = weights.get(key) || 0;
      if (!index.has(key) || weight >= existingWeight) {
        index.set(key, entry.id);
        weights.set(key, weight);
      }
    }
  }

  for (const entry of catalog.entries) {
    register(entry.id, entry, 10);
    register(entry.title, entry, 7);
    for (const alias of entry.aliases || []) register(alias, entry, 6);
    for (const address of entry.addresses || []) register(address, entry, 8);
    for (const ref of [...(entry.sourceRefs || []), ...(entry.noteRefs || [])]) {
      register(ref.path, entry, ref.entryId ? 9 : 5);
      register(ref.label, entry, ref.entryId ? 8 : 4);
      if (ref.entryId && entries.has(ref.entryId)) {
        for (const key of referenceKeys(ref.path)) {
          index.set(key, ref.entryId);
          weights.set(key, 10);
        }
      }
    }

    if (entry.kind === "text-command") {
      const opcodeAlias = (entry.aliases || []).find((alias) => /^0x[0-9a-f]{2}$/i.test(alias));
      register(opcodeAlias, entry, 12);
    }
    if (entry.kind === "symbol" && entry.title) {
      register(entry.title, entry, 12);
    }
  }

  return index;
}

function referenceKeys(value) {
  const raw = String(value || "").trim();
  if (!raw) {
    return [];
  }

  const decoded = safeDecode(raw)
    .replace(/^file:\/+/, "")
    .replace(/\\/g, "/")
    .replace(/^\/([A-Za-z]:\/)/, "$1")
    .replace(/^`|`$/g, "")
    .trim();
  const withoutHash = decoded.replace(/#.*$/, "");
  const suffix = repoRelativeSuffix(withoutHash);
  const keys = [
    decoded,
    withoutHash,
    suffix,
    suffix ? suffix.split("/").pop() : "",
    raw
  ];

  return [...new Set(keys.map(normalizeReferenceKey).filter(Boolean))];
}

function repoRelativeSuffix(value) {
  const normalized = String(value || "").replace(/\\/g, "/");
  const match = normalized.match(/(?:^|\/)(notes|src|tools|asset-manifests)\/(.+)$/i);
  return match ? `${match[1].toLowerCase()}/${match[2]}` : "";
}

function normalizeReferenceKey(value) {
  return String(value || "")
    .trim()
    .replace(/^`|`$/g, "")
    .replace(/\s+/g, " ")
    .toLowerCase();
}

function isUsefulReferenceKey(key) {
  if (!key || key.length < 3) {
    return false;
  }
  if (/^0x[0-9a-f]{2}$/i.test(key)) {
    return true;
  }
  if (/^[c-e][0-9a-f]:[0-9a-f]{4}$/i.test(key)) {
    return true;
  }
  if (/^(notes|src|tools|asset-manifests)\//i.test(key)) {
    return true;
  }
  if (/^[c-e][0-9a-f][0-9a-f]{4}[_-]/i.test(key)) {
    return true;
  }
  return key.length >= 4 && /[a-z]/i.test(key);
}

function safeDecode(value) {
  try {
    return decodeURIComponent(value);
  } catch {
    return value;
  }
}

function renderDeferredBodyLoader(entry) {
  if (!entry.bodyChunk || entry.fullBodyLoaded) {
    return "";
  }

  const size = entry.bodySize ? `${entry.bodySize.toLocaleString()} markdown characters` : "large generated body";
  const status = entry.bodyLoadError
    ? `<div class="deferredError">${escapeHtml(entry.bodyLoadError)}</div>`
    : "";
  return `
    <div class="deferredBody">
      <div>
        <div class="deferredTitle">Full body deferred</div>
        <div class="deferredText">This page starts with a compact stub. Search still uses its generated index, and the full ${escapeHtml(size)} can be loaded on demand.</div>
        ${status}
      </div>
      <button type="button" class="loadBodyButton" data-load-body-id="${escapeHtml(entry.id)}" ${entry.bodyLoading ? "disabled" : ""}>
        ${entry.bodyLoading ? "Loading..." : "Load full entry"}
      </button>
    </div>
  `;
}

function loadDeferredBody(id) {
  const entry = entries.get(id);
  if (!entry || !entry.bodyChunk || entry.fullBodyLoaded || entry.bodyLoading) {
    return;
  }

  const cachedBody = window.ENCYCLOPEDIA_ENTRY_BODIES[entry.id];
  if (cachedBody) {
    entry.body = cachedBody;
    entry.fullBodyLoaded = true;
    renderDocument();
    return;
  }

  entry.bodyLoading = true;
  entry.bodyLoadError = "";
  renderDocument();

  const script = document.createElement("script");
  script.src = entry.bodyChunk;
  script.onload = () => {
    entry.bodyLoading = false;
    const loadedBody = window.ENCYCLOPEDIA_ENTRY_BODIES[entry.id];
    if (loadedBody) {
      entry.body = loadedBody;
      entry.fullBodyLoaded = true;
      renderDocument();
      return;
    }
    entry.bodyLoadError = "The body chunk loaded, but did not publish this entry.";
    renderDocument();
  };
  script.onerror = () => {
    entry.bodyLoading = false;
    entry.bodyLoadError = "Could not load the generated body chunk.";
    renderDocument();
  };
  document.head.appendChild(script);
}

function enhanceCodeBlocks() {
  documentEl.querySelectorAll("pre").forEach((pre, index) => {
    if (pre.closest(".codeBlockWrap")) {
      return;
    }
    const lineCount = pre.querySelectorAll(".codeLine").length || (pre.textContent || "").split("\n").length;
    if (lineCount < 36) {
      return;
    }

    const wrapper = document.createElement("div");
    wrapper.className = "codeBlockWrap collapsed";
    const button = document.createElement("button");
    button.className = "codeToggle";
    button.type = "button";
    button.textContent = `Expand code (${lineCount} lines)`;
    button.setAttribute("aria-expanded", "false");
    button.addEventListener("click", () => {
      const isCollapsed = wrapper.classList.toggle("collapsed");
      button.textContent = isCollapsed ? `Expand code (${lineCount} lines)` : "Collapse code";
      button.setAttribute("aria-expanded", String(!isCollapsed));
    });

    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(button);
    wrapper.appendChild(pre);
  });
}

function renderMetaStrip(entry) {
  const chips = [
    entry.provenance ? provenanceLabel(entry.provenance) : "",
    entry.chapterScope ? chapterScopeLabel(entry.chapterScope) : "",
    ...(entry.banks || []).map((bank) => `Bank ${bank}`),
    ...(entry.addresses || []).slice(0, 3),
    entry.maturity ? maturityLabel(entry.maturity) : "",
    entry.confidence ? `Confidence: ${entry.confidence}` : "",
    entry.sourceRefs?.length ? `${entry.sourceRefs.length} source ref${entry.sourceRefs.length === 1 ? "" : "s"}` : "",
    entry.noteRefs?.length ? `${entry.noteRefs.length} note ref${entry.noteRefs.length === 1 ? "" : "s"}` : ""
  ].filter(Boolean);
  if (!chips.length) {
    return "";
  }
  return `<div class="metaStrip">${chips.map((chip) => `<span class="metaChip">${escapeHtml(chip)}</span>`).join("")}</div>`;
}

function provenanceLabel(provenance) {
  return provenanceCatalog[provenance]?.label || provenance || "Unlabeled provenance";
}

function chapterScopeLabel(scope) {
  return chapterScopeCatalog[scope]?.label || scope || "Unscoped";
}

function maturityLabel(maturity) {
  const labels = {
    curated: "Curated",
    "generated-summary": "Generated summary",
    "generated-source": "Generated source",
    "generated-asset": "Generated asset",
    "generated-tool": "Generated tool",
    "evidence-note": "Evidence note",
    "draft-narrative": "Draft narrative"
  };
  return labels[maturity] || maturity;
}

function renderRail(entry) {
  const blocks = [];
  if (currentDocumentOutline.length) {
    blocks.push(railOutlineBlock(currentDocumentOutline));
  }
  if (entry.aliases && entry.aliases.length) {
    blocks.push(railBlock("Aliases", entry.aliases));
  }
  if (entry.banks && entry.banks.length) {
    blocks.push(railBlock("Banks", entry.banks));
  }
  if (entry.addresses && entry.addresses.length) {
    blocks.push(railBlock("Addresses", entry.addresses));
  }
  if (entry.provenance) {
    blocks.push(railBlock("Provenance", [
      provenanceLabel(entry.provenance),
      provenanceCatalog[entry.provenance]?.description || ""
    ].filter(Boolean)));
  }
  if (entry.chapterScope) {
    blocks.push(railBlock("Chapter Scope", [
      chapterScopeLabel(entry.chapterScope),
      chapterScopeCatalog[entry.chapterScope]?.description || ""
    ].filter(Boolean)));
  }
  if (entry.sourceRefs && entry.sourceRefs.length) {
    blocks.push(railRefBlock("Source Evidence", entry.sourceRefs));
  }
  if (entry.noteRefs && entry.noteRefs.length) {
    blocks.push(railRefBlock("Note Evidence", entry.noteRefs));
  }
  if (entry.related && entry.related.length) {
    blocks.push(railEntryBlock("Related", entry.related));
  }
  const inboundLinks = directedGraphNeighbors(entry.id, "in", 10).map((neighbor) => neighbor.id);
  if (inboundLinks.length) {
    blocks.push(railEntryBlock("Referenced By", inboundLinks));
  }
  const graphLinks = graphNeighbors(entry.id, 8).map((neighbor) => neighbor.id);
  if (graphLinks.length) {
    blocks.push(railEntryBlock("Graph Neighbors", graphLinks));
  }
  const outlinePanel = blocks.join("") || '<div class="railBlock"><div class="railTitle">Entry</div><div class="railPill">No extra metadata yet.</div></div>';
  const favoritesPanel = renderFavoritesRail();
  const activeTab = state.railTab === "favorites" ? "favorites" : "outline";
  railEl.innerHTML = `
    <div class="railTabs" role="tablist" aria-label="Entry tools">
      <button type="button" class="railTab${activeTab === "outline" ? " active" : ""}" data-rail-tab="outline" role="tab" aria-selected="${activeTab === "outline" ? "true" : "false"}">Outline</button>
      <button type="button" class="railTab${activeTab === "favorites" ? " active" : ""}" data-rail-tab="favorites" role="tab" aria-selected="${activeTab === "favorites" ? "true" : "false"}">Favorites</button>
    </div>
    <div class="railTabPanel">
      ${activeTab === "favorites" ? favoritesPanel : outlinePanel}
    </div>
  `;

  bindEntryLinkClicks(railEl);
  railEl.querySelectorAll("[data-rail-tab]").forEach((button) => {
    button.addEventListener("click", () => {
      state.railTab = button.getAttribute("data-rail-tab") || "outline";
      renderRail(entry);
    });
  });
  railEl.querySelectorAll("[data-scroll-target]").forEach((button) => {
    button.addEventListener("click", () => navigateToDocumentSection(button.getAttribute("data-scroll-target")));
  });
}

function renderFavoritesRail() {
  const favorites = state.favorites.filter((id) => entries.has(id));
  if (favorites.length !== state.favorites.length) {
    state.favorites = favorites;
    saveFavoriteIds();
  }
  if (!favorites.length) {
    return `
      <section class="railBlock">
        <div class="railTitle">Favorites</div>
        <div class="railPill railOverflow">Star an entry title to pin it here.</div>
      </section>
    `;
  }
  return `
    <section class="railBlock">
      <div class="railTitle">Favorites</div>
      <div class="railList">
        ${favorites.map((id) => {
          const entry = entries.get(id);
          return `<button type="button" class="railPill railButton favoriteRailButton${id === state.activeId ? " active" : ""}" data-entry-id="${escapeHtml(id)}">
            <span>${escapeHtml(entry.title)}</span>
            <small>${escapeHtml(entry.kind)}</small>
          </button>`;
        }).join("")}
      </div>
    </section>
  `;
}

function railOutlineBlock(outline) {
  const limit = 32;
  const items = outline.slice(0, limit).map((item) => `
    <button type="button" class="railPill railButton railOutlineButton railOutlineLevel${item.level}" data-scroll-target="${escapeHtml(item.id)}">
      ${escapeHtml(item.title)}
    </button>
  `);
  if (outline.length > limit) {
    items.push(`<div class="railPill railOverflow">${outline.length - limit} more sections in body</div>`);
  }
  return `
    <section class="railBlock">
      <div class="railTitle">Outline</div>
      <div class="railList">${items.join("")}</div>
    </section>
  `;
}

function bindEntryLinkClicks(root, options = {}) {
  root.querySelectorAll("[data-entry-id]").forEach((button) => {
    bindEntryLinkButton(button, options);
  });
}

function bindEntryLinkButton(button, options = {}) {
  const openFromPointer = (event, forceNewTab = false) => {
    const entryId = options.entryId || button.getAttribute("data-entry-id");
    if (!entryId) {
      return;
    }
    event.preventDefault();
    openEntry(entryId, {
      event,
      newTab: forceNewTab,
      sectionId: button.getAttribute("data-section-id") || ""
    });
    if (options.afterOpen) {
      options.afterOpen(event);
    }
  };
  button.addEventListener("click", (event) => {
    if (event.button !== 0) {
      return;
    }
    openFromPointer(event);
  });
  button.addEventListener("auxclick", (event) => {
    if (event.button !== 1) {
      return;
    }
    openFromPointer(event, true);
  });
}

function navigateToDocumentSection(id) {
  if (!id) {
    return;
  }
  saveActiveScrollPosition();
  state.backStack = state.backStack || [];
  state.forwardStack = [];
  state.backStack.push(activeScrollSnapshot());
  scrollToDocumentSection(id, { updateLocationHash: true, behavior: "smooth" });
  renderNavigationButtons();
}

function scrollToDocumentSection(id, options = {}) {
  const target = id ? document.getElementById(id) : null;
  if (target) {
    resetViewportScroll();
    target.scrollIntoView({ behavior: options.behavior || "smooth", block: "start" });
    if (options.behavior === "auto") {
      window.requestAnimationFrame(() => {
        resetViewportScroll();
        target.scrollIntoView({ behavior: "auto", block: "start" });
      });
    }
    if (options.updateLocationHash) {
      updateLocation(state.activeId, id);
    }
    return true;
  }
  return false;
}

function applyPendingScroll() {
  const pending = state.pendingScroll || { type: "position", top: state.scrollPositions[state.activeId] || 0 };
  if (pending.type === "section") {
    const found = scrollToDocumentSection(pending.id, { behavior: pending.behavior || "auto" });
    if (found) {
      state.pendingScroll = null;
      saveActiveScrollPosition();
      return;
    }
    pending.attempts = (pending.attempts || 0) + 1;
    setDocumentScrollTop(0);
    state.pendingScroll = pending.attempts < 3 ? pending : null;
    return;
  }
  if (pending.type === "position") {
    setDocumentScrollTop(Math.max(0, pending.top || 0));
  } else {
    setDocumentScrollTop(0);
  }
  state.pendingScroll = null;
  saveActiveScrollPosition();
}

function setDocumentScrollTop(top) {
  resetViewportScroll();
  documentEl.scrollTop = top;
  window.requestAnimationFrame(() => {
    resetViewportScroll();
    documentEl.scrollTop = top;
    saveActiveScrollPosition();
  });
}

function resetViewportScroll() {
  window.scrollTo(0, 0);
  document.documentElement.scrollTop = 0;
  document.body.scrollTop = 0;
}

function railBlock(title, values) {
  return `
    <section class="railBlock">
      <div class="railTitle">${escapeHtml(title)}</div>
      <div class="railList">
        ${values.slice(0, 18).map((value) => `<div class="railPill">${escapeHtml(value)}</div>`).join("")}
      </div>
    </section>
  `;
}

function railRefBlock(title, refs) {
  const values = refs.slice(0, 18).map((ref) => {
    const label = ref.label || ref.path;
    if (ref.entryId && entries.has(ref.entryId)) {
      return `<button type="button" class="railPill railButton" data-entry-id="${escapeHtml(ref.entryId)}">${escapeHtml(label)}</button>`;
    }
    return `<div class="railPill">${escapeHtml(label)}</div>`;
  });
  return `
    <section class="railBlock">
      <div class="railTitle">${escapeHtml(title)}</div>
      <div class="railList">${values.join("")}</div>
    </section>
  `;
}

function railEntryBlock(title, ids) {
  const values = ids.slice(0, 18).map((id) => {
    const entry = entries.get(id);
    const label = entry ? entry.title : id;
    return entry
      ? `<button type="button" class="railPill railButton" data-entry-id="${escapeHtml(id)}">${escapeHtml(label)}</button>`
      : `<div class="railPill">${escapeHtml(label)}</div>`;
  });
  return `
    <section class="railBlock">
      <div class="railTitle">${escapeHtml(title)}</div>
      <div class="railList">${values.join("")}</div>
    </section>
  `;
}

function renderMarkdown(markdown, options = {}) {
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  const chunks = [];
  const headingCounts = new Map();
  let paragraph = [];
  let list = [];
  let table = [];
  let code = [];
  let inCode = false;
  let codeLanguage = "";

  function flushParagraph() {
    if (paragraph.length) {
      chunks.push(`<p>${formatInline(paragraph.join(" "))}</p>`);
      paragraph = [];
    }
  }

  function flushList() {
    if (list.length) {
      chunks.push(`<ul>${list.map((item) => `<li>${formatInline(item)}</li>`).join("")}</ul>`);
      list = [];
    }
  }

  function flushTable() {
    if (table.length) {
      chunks.push(renderTable(table));
      table = [];
    }
  }

  function flushCode() {
    if (code.length) {
      chunks.push(renderCodeBlock(code.join("\n"), codeLanguage));
      code = [];
      codeLanguage = "";
    }
  }

  for (const line of lines) {
    const fence = line.match(/^```\s*([A-Za-z0-9_+-]*)/);
    if (fence) {
      if (inCode) {
        inCode = false;
        flushCode();
      } else {
        flushParagraph();
        flushList();
        flushTable();
        inCode = true;
        codeLanguage = fence[1] || "";
      }
      continue;
    }

    if (inCode) {
      code.push(line);
      continue;
    }

    if (!line.trim()) {
      flushParagraph();
      flushList();
      flushTable();
      continue;
    }

    if (/^\|.*\|$/.test(line.trim())) {
      flushParagraph();
      flushList();
      table.push(line.trim());
      continue;
    }

    flushTable();

    const heading = line.match(/^(#{2,3})\s+(.+)$/);
    if (heading) {
      flushParagraph();
      flushList();
      const level = heading[1].length;
      const headingTitle = plainHeadingText(heading[2]);
      const headingId = uniqueHeadingId(headingTitle, headingCounts);
      if (options.collectHeadings) {
        currentDocumentOutline.push({ id: headingId, level, title: headingTitle });
      }
      chunks.push(`<h${level} id="${escapeHtml(headingId)}">${formatInline(heading[2])}</h${level}>`);
      continue;
    }

    const bullet = line.match(/^- (.+)$/);
    if (bullet) {
      flushParagraph();
      list.push(bullet[1]);
      continue;
    }

    paragraph.push(line.trim());
  }

  flushParagraph();
  flushList();
  flushTable();
  flushCode();
  return chunks.join("\n");
}

function plainHeadingText(value) {
  return String(value || "")
    .replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, "$2")
    .replace(/\[\[([^\]]+)\]\]/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/[*_~#]/g, "")
    .replace(/\s+/g, " ")
    .trim() || "Section";
}

function uniqueHeadingId(title, counts) {
  const base = `section-${slugText(title)}`;
  const count = (counts.get(base) || 0) + 1;
  counts.set(base, count);
  return count === 1 ? base : `${base}-${count}`;
}

function slugText(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "") || "section";
}

function renderCodeBlock(source, language) {
  const normalizedLanguage = String(language || "").toLowerCase();
  const renderedLines = String(source || "").split("\n").map((line, index) => {
    const highlighted = normalizedLanguage === "asm" || normalizedLanguage === "asar"
      ? highlightAsmLine(line)
      : normalizedLanguage === "json"
        ? highlightJsonLine(line)
      : escapeHtml(line);
    return `<span class="codeLine"><span class="lineText">${highlighted || " "}</span></span>`;
  }).join("");
  const languageClass = normalizedLanguage ? ` codeBlock-${escapeHtml(normalizedLanguage)}` : "";
  const languageAttribute = normalizedLanguage ? ` data-language="${escapeHtml(normalizedLanguage)}"` : "";
  return `<pre class="codeBlock codeBlockLines${languageClass}"><code${languageAttribute}>${renderedLines}</code></pre>`;
}

function highlightJsonLine(line) {
  return escapeHtml(line).replace(/(&quot;(?:\\.|[^&])*?&quot;)(\s*:)?|(-?\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?\b)|\b(true|false|null)\b/g, (match, stringValue, keyColon, numberValue, literalValue) => {
    if (stringValue && keyColon) {
      return `<span class="jsonKey">${stringValue}</span>${keyColon}`;
    }
    if (stringValue) {
      return `<span class="jsonString">${stringValue}</span>`;
    }
    if (numberValue) {
      return `<span class="jsonNumber">${numberValue}</span>`;
    }
    if (literalValue) {
      return `<span class="jsonLiteral">${literalValue}</span>`;
    }
    return match;
  });
}

function highlightAsmLine(line) {
  const commentIndex = line.indexOf(";");
  const codePart = commentIndex === -1 ? line : line.slice(0, commentIndex);
  const commentPart = commentIndex === -1 ? "" : line.slice(commentIndex);
  return `${highlightAsmCode(codePart)}${commentPart ? `<span class="asmComment">${escapeHtml(commentPart)}</span>` : ""}`;
}

function highlightAsmCode(value) {
  return String(value || "").replace(/([A-Za-z_.$][A-Za-z0-9_.$]*:)|("(?:\\.|[^"])*"|'(?:\\.|[^'])*')|(#?\$[0-9A-Fa-f]+|%[01]+|#?\b\d+\b)|(\.[A-Za-z_][A-Za-z0-9_.]*\b)|\b([A-Za-z_][A-Za-z0-9_]*)\b/g, (match, label, stringValue, numberValue, directive, word) => {
    if (label) {
      return `<span class="asmLabel">${escapeHtml(label)}</span>`;
    }
    if (stringValue) {
      return `<span class="asmString">${escapeHtml(stringValue)}</span>`;
    }
    if (numberValue) {
      return `<span class="asmNumber">${escapeHtml(numberValue)}</span>`;
    }
    if (directive) {
      return `<span class="asmDirective">${escapeHtml(directive)}</span>`;
    }
    if (word && isAsmMnemonic(word)) {
      return `<span class="asmMnemonic">${escapeHtml(word)}</span>`;
    }
    if (word && isAsmKeyword(word)) {
      return `<span class="asmDirective">${escapeHtml(word)}</span>`;
    }
    return escapeHtml(match);
  });
}

function isAsmMnemonic(value) {
  return ASM_MNEMONICS.has(String(value || "").toLowerCase());
}

function isAsmKeyword(value) {
  return ASM_KEYWORDS.has(String(value || "").toLowerCase());
}

function renderTable(rows) {
  const parsed = rows
    .filter((row) => !/^\|\s*-+/.test(row))
    .map((row) => row.slice(1, -1).split("|").map((cell) => cell.trim()));
  if (!parsed.length) {
    return "";
  }
  const [head, ...body] = parsed;
  return `
    <table>
      <thead><tr>${head.map((cell) => `<th>${formatInline(cell)}</th>`).join("")}</tr></thead>
      <tbody>${body.map((row) => `<tr>${row.map((cell) => `<td>${formatInline(cell)}</td>`).join("")}</tr>`).join("")}</tbody>
    </table>
  `;
}

function formatInline(text) {
  const placeholders = [];
  const withMarkdownLinks = String(text).replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, href) => {
    const index = placeholders.length;
    const linkTarget = entryLinkTarget(href) || entryLinkTarget(label);
    if (linkTarget) {
      placeholders.push(renderEntryButton(label, linkTarget));
    } else {
      placeholders.push(renderExternalLink(label, href));
    }
    return `@@LINK_${index}@@`;
  });

  const escaped = escapeHtml(withMarkdownLinks)
    .replace(/`([^`]+)`/g, (_, value) => renderInlineCode(value, placeholders))
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, (_, rawId, label) => {
      const index = placeholders.length;
      const target = parseEntryTarget(rawId);
      placeholders.push(renderEntryButton(label, target));
      return `@@LINK_${index}@@`;
    })
    .replace(/\[\[([^\]]+)\]\]/g, (_, rawId) => {
      const index = placeholders.length;
      const target = parseEntryTarget(rawId);
      const entry = entries.get(target.id);
      placeholders.push(renderEntryButton(entry ? entry.title : target.id, target));
      return `@@LINK_${index}@@`;
    });

  return placeholders.reduce((html, value, index) => html.replace(`@@LINK_${index}@@`, value), escaped);
}

function entryLinkTarget(value) {
  const target = parseEntryTarget(String(value || "").replace(/^#/, ""));
  if (target.id && entries.has(target.id)) {
    return target;
  }
  const entryId = resolveReference(value);
  return entryId ? { id: entryId, sectionId: "" } : null;
}

function renderEntryButton(label, target) {
  const section = target.sectionId ? ` data-section-id="${escapeHtml(target.sectionId)}"` : "";
  return `<button type="button" class="docLink" data-entry-id="${escapeHtml(target.id)}"${section}>${escapeHtml(label)}</button>`;
}

function renderInlineCode(value, placeholders) {
  const entryId = resolveReference(value);
  if (!entryId) {
    return `<code>${value}</code>`;
  }
  const index = placeholders.length;
  placeholders.push(`<button type="button" class="docLink inlineCodeLink" data-entry-id="${escapeHtml(entryId)}"><code>${value}</code></button>`);
  return `@@LINK_${index}@@`;
}

function renderExternalLink(label, href) {
  const safeHref = String(href || "").trim();
  if (!/^https?:\/\//i.test(safeHref)) {
    return escapeHtml(label);
  }
  return `<a href="${escapeHtml(safeHref)}" target="_blank" rel="noreferrer">${escapeHtml(label)}</a>`;
}

function resolveReference(value) {
  for (const key of referenceKeys(value)) {
    const id = referenceIndex.get(key);
    if (id && entries.has(id)) {
      return id;
    }
  }
  return "";
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function search(query, limit = 9) {
  const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
  if (!terms.length) {
    return [];
  }

  return catalog.entries
    .map((entry) => {
      const haystack = entry.searchText || "";
      let score = 0;
      for (const term of terms) {
        if (entry.title.toLowerCase().includes(term)) score += 8;
        if (entry.title.toLowerCase().startsWith(term)) score += 10;
        if (entry.kind.toLowerCase() === term) score += 30;
        if ((entry.aliases || []).some((alias) => alias.toLowerCase().includes(term))) score += 6;
        if ((entry.addresses || []).some((address) => address.toLowerCase().includes(term))) score += 6;
        if (haystack.includes(term)) score += 1;
      }
      return { entry, score };
    })
    .filter((result) => result.score > 0)
    .sort((a, b) => b.score - a.score || a.entry.title.localeCompare(b.entry.title))
    .slice(0, limit === Infinity ? undefined : limit);
}

function renderSearchResults(results) {
  if (!results.length) {
    searchResults.hidden = true;
    searchResults.innerHTML = "";
    currentSearchResults = [];
    searchSelectionIndex = 0;
    return;
  }

  const fullResultsId = "search-results";
  currentSearchResults = [
    ...results.map(({ entry }) => entry.id),
    fullResultsId
  ];
  searchSelectionIndex = Math.max(0, Math.min(searchSelectionIndex, currentSearchResults.length - 1));
  searchResults.hidden = false;
  searchResults.innerHTML = [
    ...results.map(({ entry }, index) => `
      <button type="button" class="searchItem${index === searchSelectionIndex ? " active" : ""}" data-entry-id="${escapeHtml(entry.id)}" data-search-index="${index}" aria-selected="${index === searchSelectionIndex ? "true" : "false"}">
        <div class="searchItemTitle">${escapeHtml(entry.title)}</div>
        <div class="searchItemMeta">${escapeHtml(entry.kind)}${entry.banks && entry.banks.length ? ` - ${escapeHtml(entry.banks.join(", "))}` : ""}</div>
      </button>
    `),
    `<button type="button" class="searchItem${searchSelectionIndex === results.length ? " active" : ""}" data-entry-id="${fullResultsId}" data-search-index="${results.length}" aria-selected="${searchSelectionIndex === results.length ? "true" : "false"}">
      <div class="searchItemTitle">Open full search results</div>
      <div class="searchItemMeta">View linked result set in a tab</div>
    </button>`
  ].join("");

  const resultEntry = entries.get(fullResultsId);
  if (resultEntry) {
    const fullResults = search(searchInput.value, FULL_RESULTS_LIMIT);
    const grouped = new Map();
    for (const { entry } of fullResults) {
      grouped.set(entry.kind, [...(grouped.get(entry.kind) || []), entry]);
    }
    const totalMatches = search(searchInput.value, Infinity).length;
    const capNote = totalMatches > fullResults.length
      ? `Showing first ${fullResults.length} of ${totalMatches} matches. Narrow the query to see more specific results.`
      : `Showing all ${totalMatches} matches.`;
    resultEntry.summary = `${totalMatches} results for "${searchInput.value}".`;
    resultEntry.body = [
      capNote,
      "",
      catalog.deferredBodyCount ? `Search includes a compact generated index for ${catalog.deferredBodyCount} deferred heavy entries. Open a result and load the full entry when you need the complete body.` : "",
      "",
      ...[...grouped.entries()].sort(([a], [b]) => kindRank(a) - kindRank(b)).map(([kind, group]) => [
      `## ${kind}`,
      group.map((entry) => `- [[${entry.id}|${entry.title}]] - ${entry.summary || entry.kind}`).join("\n")
      ].join("\n"))
    ].join("\n\n");
  }

  bindEntryLinkClicks(searchResults, {
    afterOpen: () => {
      searchResults.hidden = true;
    }
  });
  searchResults.querySelectorAll("[data-search-index]").forEach((button) => {
    button.addEventListener("mouseenter", () => {
      searchSelectionIndex = Number(button.getAttribute("data-search-index")) || 0;
      searchResults.querySelectorAll(".searchItem").forEach((item, index) => {
        const active = index === searchSelectionIndex;
        item.classList.toggle("active", active);
        item.setAttribute("aria-selected", active ? "true" : "false");
      });
    });
  });
}

function openSearchSelection() {
  const entryId = currentSearchResults[searchSelectionIndex];
  if (!entryId || !entries.has(entryId)) {
    return;
  }
  openEntry(entryId);
  searchResults.hidden = true;
  searchInput.blur();
}

function kindRank(kind) {
  const index = KIND_ORDER.indexOf(kind);
  return index === -1 ? KIND_ORDER.length : index;
}

searchInput.addEventListener("input", (event) => {
  searchSelectionIndex = 0;
  renderSearchResults(search(event.target.value, 9));
});

searchInput.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    searchResults.hidden = true;
    searchInput.blur();
    return;
  }
  if (searchResults.hidden || !currentSearchResults.length) {
    return;
  }
  if (event.key === "ArrowDown") {
    event.preventDefault();
    searchSelectionIndex = (searchSelectionIndex + 1) % currentSearchResults.length;
    renderSearchResults(search(searchInput.value, 9));
  } else if (event.key === "ArrowUp") {
    event.preventDefault();
    searchSelectionIndex = (searchSelectionIndex - 1 + currentSearchResults.length) % currentSearchResults.length;
    renderSearchResults(search(searchInput.value, 9));
  } else if (event.key === "Enter") {
    event.preventDefault();
    openSearchSelection();
  }
});

document.addEventListener("click", (event) => {
  if (!event.target.closest(".searchWrap")) {
    searchResults.hidden = true;
  }
});

window.addEventListener("hashchange", () => {
  const { id, sectionId } = parseLocationTarget();
  if (!id || !entries.has(id)) {
    return;
  }
  if (id === state.activeId) {
    if (sectionId) {
      scrollToDocumentSection(sectionId, { behavior: "auto" });
    }
    return;
  }
  saveActiveScrollPosition();
  if (!state.tabs.includes(id)) {
    const activeIndex = Math.max(0, state.tabs.indexOf(state.activeId));
    state.tabs[activeIndex] = id;
  }
  state.activeId = id;
  state.pendingScroll = sectionId
    ? { type: "section", id: sectionId, behavior: "auto", attempts: 0 }
    : { type: "top" };
  render();
});

function render() {
  renderNavigationButtons();
  renderToc();
  renderTabs();
  renderDocument();
  saveWorkspaceState();
}

function renderNavigationButtons() {
  backButton.disabled = !(state.backStack && state.backStack.length);
  forwardButton.disabled = !(state.forwardStack && state.forwardStack.length);
  renderWorkspaceButton();
  renderBuildStatusButton();
}

function renderWorkspaceButton() {
  if (!workspaceButton) {
    return;
  }
  const ready = workspaceIsReady();
  workspaceButton.textContent = ready ? "Workspace ready" : "Add ROM";
  workspaceButton.classList.toggle("ready", ready);
  workspaceButton.title = ready
    ? "Open local ROM workspace"
    : "Add a ROM or open notes-only workspace setup";
}

function renderBuildStatusButton() {
  if (!buildStatusButton) {
    return;
  }
  const mode = catalog.buildMode || "local";
  const label = mode === "authored" ? "Authored" : "Local";
  const target = "catalog-build-status";
  buildStatusButton.textContent = `${label} catalog`;
  buildStatusButton.dataset.entryId = target;
  buildStatusButton.classList.toggle("local", mode !== "authored");
  buildStatusButton.title = mode === "authored"
    ? "Authored release baseline. Open release artifact policy."
    : "Local generated catalog. Open ROM and generated content status.";
}

backButton.addEventListener("click", goBack);
forwardButton.addEventListener("click", goForward);
if (workspaceButton) {
  workspaceButton.addEventListener("click", () => {
    openEntry(entries.has("local-workspace") ? "local-workspace" : "overview");
  });
}
if (buildStatusButton) {
  buildStatusButton.addEventListener("click", () => {
    const target = buildStatusButton.dataset.entryId || "release-artifact-policy";
    openEntry(entries.has(target) ? target : "overview");
  });
}

render();
