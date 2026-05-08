const catalog = window.ENCYCLOPEDIA_CATALOG || { entries: [] };
window.ENCYCLOPEDIA_ENTRY_BODIES = window.ENCYCLOPEDIA_ENTRY_BODIES || {};
window.ENCYCLOPEDIA_DEFERRED_DATA = window.ENCYCLOPEDIA_DEFERRED_DATA || {};
const provenanceCatalog = catalog.provenanceCatalog || {};
const chapterScopeCatalog = catalog.chapterScopeCatalog || {};
const PRIVATE_REFERENCE_MODE = catalog.buildMode === "private";
const SEARCH_FACETS = [
  { id: "all", label: "All", kinds: [] },
  { id: "notes", label: "Notes", kinds: ["note", "reference-script", "reference-document", "reference-table"] },
  { id: "source", label: "Source", kinds: ["source", "source-file", "reference-source"] },
  { id: "symbols", label: "Routines/Symbols", kinds: ["routine", "symbol"] },
  { id: "systems", label: "Systems", kinds: ["chapter", "topic", "bank", "script-vm", "text-command", "asset-contract"] },
  { id: "tools", label: "Tools/Validation", kinds: ["workflow", "tool"] },
  { id: "manifests", label: "Manifests", kinds: ["asset-manifest"] }
];
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
const searchDocuments = new Map((catalog.searchIndex?.documents || []).map((document) => [document.id, document]));
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
const FAVORITES_STATE_KEY = "earthbound-encyclopedia-favorites-v1";
const READER_FOCUS_STATE_KEY = "earthbound-encyclopedia-reader-focus-v1";
const state = {
  tabs: ["overview"],
  activeId: "overview",
  graphFocusId: "overview",
  railTab: "outline",
  searchFacet: "all",
  tableSort: {},
  railExpanded: {},
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
  "reference-source",
  "symbol",
  "routine",
  "tool",
  "note",
  "reference-script",
  "reference-document",
  "reference-table",
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
const buildStatusButton = document.getElementById("buildStatusButton");
let currentDocumentOutline = [];
let currentSearchResults = [];
let searchSelectionIndex = 0;
state.favorites = loadFavoriteIds();
state.readerFocusMode = loadReaderFocusMode();
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

function loadReaderFocusMode() {
  try {
    const value = window.localStorage.getItem(READER_FOCUS_STATE_KEY);
    return ["auto", "focus", "details"].includes(value) ? value : "auto";
  } catch {
    return "auto";
  }
}

function saveReaderFocusMode() {
  try {
    window.localStorage.setItem(READER_FOCUS_STATE_KEY, state.readerFocusMode || "auto");
  } catch {
    // Reader focus is a preference; the app remains usable without persistence.
  }
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
  const seen = new Set();
  const configured = Array.isArray(catalog.navSections) && catalog.navSections.length
    ? catalog.navSections
    : [
        { title: "Overview", ids: ["overview", "catalog-build-status", "upstream-status", "narrative-index", "learning-path-index"] },
        { title: "Source", ids: ["source-browser", "source-tree", "reference-source-browser", "routine-index", "bank-map"] },
        { title: "Notes", ids: ["note-index", "reference-library", "reference-tables", "script-source-index"] },
        { title: "Systems", ids: ["systems-hub", "topic-index"] },
        { title: "Tools/Validation", ids: ["workflows", "tool-index"] }
      ];
  const groups = configured.map((section) => {
    const sectionEntries = (section.ids || [])
      .map((id) => entries.get(id))
      .filter((entry) => isContentVisible(entry) && entry.showInToc !== false && !seen.has(entry.id));
    for (const entry of sectionEntries) {
      seen.add(entry.id);
    }
    return { title: section.title, entries: sectionEntries };
  }).filter((group) => group.entries.length > 0);

  const favorites = (state.favorites || [])
    .map((id) => entries.get(id))
    .filter((entry) => isContentVisible(entry) && !seen.has(entry.id));
  if (favorites.length) {
    groups.unshift({ title: "Pinned", entries: favorites });
  }
  return groups;
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
    applyReaderFocusLayout(false);
    documentEl.innerHTML = '<div class="emptyState">Entry not found.</div>';
    railEl.innerHTML = "";
    currentDocumentOutline = [];
    return;
  }

  currentDocumentOutline = [];
  const readerFocused = shouldUseReaderFocus(entry);
  applyReaderFocusLayout(readerFocused);
  documentEl.innerHTML = `
    <div class="docInner${isWideReaderEntry(entry) || readerFocused ? " wideDoc" : ""}">
      ${renderFirstRunPrompt()}
      <div class="entryKind">${escapeHtml(entry.kind)}</div>
      <div class="titleRow">
        <h1>${escapeHtml(entry.title)}</h1>
        ${renderFavoriteButton(entry)}
        ${renderReaderFocusButton(readerFocused)}
      </div>
      ${renderMetaStrip(entry)}
      ${shouldRenderSummary(entry) ? `<p>${escapeHtml(entry.summary)}</p>` : ""}
      ${renderEntryBody(entry)}
      ${entry.sourceFile ? "" : renderDeferredBodyLoader(entry)}
      ${renderReferenceWorkbench(entry)}
      ${entry.id === "relationship-graph" ? renderRelationshipGraphDocument() : renderEntryGraphPreview(entry)}
    </div>
  `;

  bindEntryLinkClicks(documentEl);
  documentEl.querySelectorAll("[data-favorite-id]").forEach((button) => {
    button.addEventListener("click", () => toggleFavorite(button.getAttribute("data-favorite-id")));
  });
  documentEl.querySelectorAll("[data-reader-focus-toggle]").forEach((button) => {
    button.addEventListener("click", () => toggleReaderFocusPreference(readerFocused));
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
  documentEl.querySelectorAll("[data-load-data-key]").forEach((button) => {
    button.addEventListener("click", () => loadDeferredData(button.getAttribute("data-load-data-key"), button.getAttribute("data-load-data-chunk")));
  });
  documentEl.querySelectorAll("[data-source-sort]").forEach((button) => {
    button.addEventListener("click", () => {
      const key = button.getAttribute("data-source-sort");
      const current = state.tableSort[entry.id] || { key: "address", direction: "asc" };
      state.tableSort[entry.id] = {
        key,
        direction: current.key === key && current.direction === "asc" ? "desc" : "asc"
      };
      renderDocument();
    });
  });
  documentEl.querySelectorAll("[data-copy-text]").forEach((button) => {
    button.addEventListener("click", async () => {
      const value = button.getAttribute("data-copy-text") || "";
      try {
        await navigator.clipboard.writeText(value);
        button.textContent = "Copied";
        window.setTimeout(() => { button.textContent = button.getAttribute("data-copy-label") || "Copy"; }, 900);
      } catch {
        button.textContent = "Copy failed";
      }
    });
  });
  documentEl.querySelectorAll("[data-scroll-target]").forEach((button) => {
    button.addEventListener("click", () => navigateToDocumentSection(button.getAttribute("data-scroll-target")));
  });
  enhanceCodeBlocks();

  renderRail(entry);
  applyPendingScroll();
  scheduleDeferredBodyAutoLoad(entry);
}

function isWideReaderEntry(entry) {
  return Boolean(entry.sourceFile || entry.kind === "reference-script" || entry.kind === "source");
}

function isReaderFocusCandidate(entry) {
  if (!entry) {
    return false;
  }
  return Boolean(
    entry.sourceFile
    || entry.kind === "reference-script"
    || entry.bodySize >= 12000
    || (entry.fullBodyLoaded && String(entry.body || "").length >= 12000)
  );
}

function shouldUseReaderFocus(entry) {
  if (state.readerFocusMode === "focus") {
    return true;
  }
  if (state.readerFocusMode === "details") {
    return false;
  }
  return isReaderFocusCandidate(entry);
}

function applyReaderFocusLayout(isFocused) {
  const shell = documentEl?.closest(".documentShell");
  if (shell) {
    shell.classList.toggle("readerFocus", Boolean(isFocused));
  }
}

function renderReaderFocusButton(isFocused) {
  return `
    <button type="button" class="readerFocusButton" data-reader-focus-toggle title="${isFocused ? "Show the details rail" : "Hide the details rail and widen the reader"}">
      ${isFocused ? "Show details" : "Focus"}
    </button>
  `;
}

function toggleReaderFocusPreference(isFocused) {
  state.readerFocusMode = isFocused ? "details" : "focus";
  saveReaderFocusMode();
  renderDocument();
}

function scheduleDeferredBodyAutoLoad(entry) {
  if (!entry.bodyChunk || entry.fullBodyLoaded || entry.bodyLoading || entry.bodyLoadError) {
    return;
  }
  window.setTimeout(() => {
    const activeEntry = entries.get(state.activeId);
    if (activeEntry?.id === entry.id) {
      loadDeferredBody(entry.id);
    }
  }, 0);
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
  return "";
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
  if (entry.id === "narrative-index") {
    return renderNarrativeHub();
  }
  if (entry.id === "learning-path-index") {
    return renderLearningPathIndex();
  }
  if (entry.id === "topic-index") {
    return renderTopicHub();
  }
  if (entry.id === "systems-hub") {
    return renderSystemsHub();
  }
  if (entry.id === "source-browser") {
    return renderSourceBrowserHub();
  }
  if (entry.id === "reference-snapshot") {
    return renderReferenceSnapshot(entry);
  }
  if (entry.sourceBank) {
    return renderSourceBankPage(entry);
  }
  if (entry.sourceFile) {
    return renderSourceFileReader(entry);
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
    .filter((entry) => isContentVisible(entry) && entry.kind === "narrative")
    .sort((a, b) => (a.tocPriority ?? 50) - (b.tocPriority ?? 50) || a.title.localeCompare(b.title));
  const learningPaths = catalog.entries
    .filter((entry) => isContentVisible(entry) && entry.kind === "learning-path" && entry.id !== "learning-path-index" && entry.learningPath)
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

function renderTopicHub() {
  const headingCounts = new Map();
  const topicSectionId = registerHubSection("Topic Areas", headingCounts);
  const supportingSectionId = registerHubSection("Supporting Indexes", headingCounts);
  const topics = catalog.entries
    .filter((entry) => isContentVisible(entry) && entry.kind === "topic" && entry.id !== "topic-index")
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
          ${supportIds.filter((id) => isContentVisible(entries.get(id))).map((id) => renderHubCard(entries.get(id), {
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
    .filter((entry) => isContentVisible(entry) && /^source-bank-[c-e][0-9a-f]$/i.test(entry.id))
    .sort((a, b) => (a.banks?.[0] || "").localeCompare(b.banks?.[0] || ""));
  const comparisonSectionId = registerHubSection("Comparison Source", headingCounts);
  const indexIds = ["source-tree", "routine-index", "bank-map", "relationship-graph", "workflows"];
  return `
    <section class="hubPage">
      <section class="hubSection" id="${escapeHtml(bankSectionId)}">
        <div class="hubSectionHeader">
          <h2>Source Banks</h2>
          <p>Bank-level entry points into checked-in source files, routine pages, and scaffold/data files.</p>
        </div>
        ${renderSourceBankOverview(sourceBanks)}
      </section>
      <section class="hubSection" id="${escapeHtml(comparisonSectionId)}">
        <div class="hubSectionHeader">
          <h2>Comparison Source</h2>
          <p>Traditional source references that sit alongside the current decomp source browser.</p>
        </div>
        <div class="hubGrid compact">
          ${["reference-source-browser", "script-source-index"].filter((id) => isContentVisible(entries.get(id))).map((id) => renderHubCard(entries.get(id), {
            eyebrow: displayKindLabel(entries.get(id)),
            meta: evidenceMeta(entries.get(id))
          })).join("")}
        </div>
      </section>
      <section class="hubSection" id="${escapeHtml(indexSectionId)}">
        <div class="hubSectionHeader">
          <h2>Source Indexes</h2>
          <p>Higher-level maps for moving from source files into routines, workflows, validation, and relationships.</p>
        </div>
        <div class="hubGrid compact">
          ${indexIds.filter((id) => isContentVisible(entries.get(id))).map((id) => renderHubCard(entries.get(id), {
            eyebrow: entries.get(id).kind,
            meta: evidenceMeta(entries.get(id))
          })).join("")}
        </div>
      </section>
    </section>
  `;
}

function renderSourceBankOverview(sourceBanks) {
  if (!sourceBanks.length) {
    return `<div class="emptyState">No source banks indexed.</div>`;
  }
  return `
    <div class="denseTableWrap">
      <table class="denseTable sourceBankOverview">
        <thead>
          <tr><th>Bank</th><th>Files</th><th>Routines</th><th>Scaffold/Data</th><th>Open</th></tr>
        </thead>
        <tbody>
          ${sourceBanks.map((entry) => {
            const bank = entry.sourceBank?.bank || entry.banks?.[0] || "";
            return `<tr>
              <td><code>${escapeHtml(bank)}</code></td>
              <td>${Number(entry.sourceBank?.fileCount || 0).toLocaleString()}</td>
              <td>${Number(entry.sourceBank?.routineCount || 0).toLocaleString()}</td>
              <td>${Number(entry.sourceBank?.scaffoldCount || 0).toLocaleString()}</td>
              <td><button type="button" class="tableEntryLink" data-entry-id="${escapeHtml(entry.id)}">Open bank</button></td>
            </tr>`;
          }).join("")}
        </tbody>
      </table>
    </div>
  `;
}

function renderReferenceSnapshot(entry) {
  const sync = catalog.referenceSync || {};
  const git = sync.sourceGit || {};
  const counts = Object.entries(sync.counts || {}).sort((a, b) => a[0].localeCompare(b[0]));
  const rows = [
    ["Synced", sync.generatedAt || catalog.generatedAt || "unknown"],
    ["Source", sync.sourceRoot || catalog.sourceRoot || "bundled-private-reference"],
    ["Copied", Number(sync.copiedFiles || 0).toLocaleString()],
    ["Skipped", Number(sync.skippedEntries || 0).toLocaleString()],
    ["Git branch", git.available ? git.branch || "unknown" : "unavailable"],
    ["Git commit", git.available ? git.shortSha || git.sha || "unknown" : "unavailable"],
    ["Dirty checkout", git.available ? (git.dirty ? "yes" : "no") : "unknown"]
  ];
  return `
    <section class="snapshotPanel">
      <h2>Reference Snapshot</h2>
      <p>${escapeHtml(entry.summary || "Bundled reference provenance.")}</p>
      ${renderKeyValueTable(rows)}
      <h2>Included Roots</h2>
      <div class="compactList">
        ${(sync.includedRoots || []).map((root) => `<span>${escapeHtml(root)}</span>`).join("")}
      </div>
      <h2>Reference Counts</h2>
      ${counts.length ? renderKeyValueTable(counts.map(([root, count]) => [root, `${Number(count).toLocaleString()} files`])) : "<p>No per-root counts were recorded.</p>"}
      <h2>Excluded Payloads</h2>
      <p>${escapeHtml(sync.excludedPolicy || "ROMs, generated binary/media payloads, caches, dumps, tools/, and executable tool scripts are excluded.")}</p>
    </section>
  `;
}

function renderSystemsHub() {
  const domains = [
    ["Text/Scripting", "Text commands, localization, action/event scripts, 1995 .MSG references, and VM semantics.", ["topic-localization-authoring", "topic-actionscript-events", "script-source-index", "script-and-text-vms", "text-command-vm"]],
    ["Battle", "Battle dispatch, PSI/menu flow, enemy data, text, and visual contracts.", ["topic-battle-runtime", "bank-c2"]],
    ["Overworld", "Entities, movement, camera, collision, teleport, doors, and map interaction.", ["topic-overworld-runtime", "bank-c0"]],
    ["Audio", "Music/audio packs, APU transfer evidence, and sound-data documentation.", ["topic-audio-data"]],
    ["UI/Windows", "Menus, windows, fonts, tile staging, presentation effects, and HDMA helpers.", ["topic-ui-rendering", "bank-c1", "bank-c4"]],
    ["Data/Manifests", "Data contracts, tables, graphics/map/audio manifest documentation, and payload-free inventories.", ["asset-contracts", "asset-manifest-index", "topic-asset-pipeline"]]
  ];
  return `
    <section class="hubPage systemsHub">
      <section class="hubSection">
        <div class="hubSectionHeader">
          <h2>Domains</h2>
          <p>Generated entries stay searchable, but system navigation starts from practical domains.</p>
        </div>
        <div class="domainList">
          ${domains.map(([title, summary, ids]) => renderDomainRow(title, summary, ids)).join("")}
        </div>
      </section>
      <section class="hubSection">
        <div class="hubSectionHeader">
          <h2>Dense Indexes</h2>
          <p>Use these when you need raw generated coverage.</p>
        </div>
        ${renderCompactEntryList(["topic-index", "bank-map", "asset-manifest-index", "routine-index"].filter((id) => isContentVisible(entries.get(id))).map((id) => entries.get(id)))}
      </section>
    </section>
  `;
}

function renderDomainRow(title, summary, ids) {
  const linked = ids.filter((id) => isContentVisible(entries.get(id))).map((id) => entries.get(id));
  const count = catalog.facets?.domainCounts?.[title] || linked.length;
  return `
    <article class="domainRow">
      <div>
        <h3>${escapeHtml(title)}</h3>
        <p>${escapeHtml(summary)}</p>
      </div>
      <div class="domainMeta">${Number(count).toLocaleString()} indexed</div>
      <div class="domainLinks">
        ${linked.map((entry) => `<button type="button" class="inlineEntryButton" data-entry-id="${escapeHtml(entry.id)}">${escapeHtml(entry.title)}</button>`).join("")}
      </div>
    </article>
  `;
}

function renderSourceBankPage(entry) {
  const sourceBank = entry.sourceBank || {};
  const key = sourceBank.bankFilesKey;
  const rows = window.ENCYCLOPEDIA_DEFERRED_DATA[key] || sourceBank.previewFiles || [];
  const fullLoaded = Boolean(window.ENCYCLOPEDIA_DEFERRED_DATA[key]);
  const sort = state.tableSort[entry.id] || { key: "address", direction: "asc" };
  const sortedRows = sortSourceRows(rows, sort);
  const loadPanel = fullLoaded ? "" : `
    <div class="deferredBody">
      <div>
        <div class="deferredTitle">Full bank file table deferred</div>
        <div class="deferredText">Showing ${rows.length} preview files. Load the full ${Number(sourceBank.fileCount || rows.length).toLocaleString()} file table when you need dense source navigation.</div>
        ${entry.dataLoadError ? `<div class="deferredError">${escapeHtml(entry.dataLoadError)}</div>` : ""}
      </div>
      <button type="button" class="loadBodyButton" data-load-data-key="${escapeHtml(key)}" data-load-data-chunk="${escapeHtml(sourceBank.bankFilesChunk || "")}" ${entry.dataLoading ? "disabled" : ""}>
        ${entry.dataLoading ? "Loading..." : "Load file table"}
      </button>
    </div>
  `;
  return `
    <section class="sourceBankPage">
      <div class="sourceStatsBar">
        <span>${Number(sourceBank.fileCount || rows.length).toLocaleString()} files</span>
        <span>${Number(sourceBank.routineCount || 0).toLocaleString()} routines</span>
        <span>${Number(sourceBank.scaffoldCount || 0).toLocaleString()} scaffold/data</span>
      </div>
      ${renderSourceFileTable(sortedRows, sort)}
      ${loadPanel}
    </section>
  `;
}

function sortSourceRows(rows, sort) {
  const direction = sort.direction === "desc" ? -1 : 1;
  return [...rows].sort((a, b) => {
    const left = a[sort.key] ?? "";
    const right = b[sort.key] ?? "";
    const compare = typeof left === "number" && typeof right === "number"
      ? left - right
      : String(left).localeCompare(String(right));
    return compare * direction || String(a.path || "").localeCompare(String(b.path || ""));
  });
}

function renderSourceFileTable(rows, sort) {
  if (!rows.length) {
    return `<div class="emptyState">No source files indexed for this bank.</div>`;
  }
  const columns = [
    ["address", "Address"],
    ["path", "Path"],
    ["role", "Role"],
    ["lineCount", "Lines"],
    ["labelCount", "Labels"],
    ["sourceUnitCount", "Units"],
    ["relatedNoteCount", "Notes"]
  ];
  return `
    <div class="denseTableWrap">
      <table class="denseTable sourceFileTable">
        <thead>
          <tr>${columns.map(([key, label]) => `<th><button type="button" data-source-sort="${escapeHtml(key)}">${escapeHtml(label)}${sort.key === key ? (sort.direction === "asc" ? " ^" : " v") : ""}</button></th>`).join("")}</tr>
        </thead>
        <tbody>
          ${rows.map((row) => `<tr>
            <td>${row.address ? `<code>${escapeHtml(row.address)}</code>` : ""}</td>
            <td><button type="button" class="tableEntryLink" data-entry-id="${escapeHtml(row.id)}">${escapeHtml(row.path || row.title || row.id)}</button></td>
            <td>${escapeHtml(row.role || "")}</td>
            <td>${Number(row.lineCount || 0).toLocaleString()}</td>
            <td>${Number(row.labelCount || 0).toLocaleString()}</td>
            <td>${Number(row.sourceUnitCount || 0).toLocaleString()}</td>
            <td>${Number(row.relatedNoteCount || 0).toLocaleString()}</td>
          </tr>`).join("")}
        </tbody>
      </table>
    </div>
  `;
}

function renderSourceFileReader(entry) {
  const file = entry.sourceFile || {};
  const code = entry.deferredBody && !entry.fullBodyLoaded ? "" : sourceCodeFromBody(entry.body || "");
  const labelAnchors = code ? sourceLabelAnchorsFromCode(code) : new Map();
  return `
    <section class="sourceReader">
      <div class="sourceReaderHeader">
        <div>
          <div class="sourcePath">${escapeHtml(file.path || entry.title)}</div>
          <div class="sourceReaderMeta">
            <span>${escapeHtml(file.bank ? `Bank ${file.bank}` : "Source")}</span>
            <span>${escapeHtml(file.role || "source")}</span>
            <span>${Number(file.lineCount || 0).toLocaleString()} lines</span>
            <span>${Number(file.labelCount || 0).toLocaleString()} labels</span>
          </div>
        </div>
        <div class="sourceReaderActions">
          ${file.path ? `<button type="button" class="hubCardAction secondary" data-copy-text="${escapeHtml(file.path)}" data-copy-label="Copy path">Copy path</button>` : ""}
          ${file.firstAddress ? `<button type="button" class="hubCardAction secondary" data-copy-text="${escapeHtml(file.firstAddress)}" data-copy-label="Copy address">Copy address</button>` : ""}
        </div>
      </div>
      <div class="sourceReaderGrid">
        <aside class="sourceOutlinePanel">
          ${renderSourceOutline(file, labelAnchors)}
        </aside>
        <div class="sourceCodePanel">
          ${code ? renderCodeBlock(code, "asm") : `<div class="sourcePlaceholder">Full source is loaded on demand.</div>${renderDeferredBodyLoader(entry)}`}
        </div>
      </div>
      ${entry.deferredBody && !entry.fullBodyLoaded && !entry.bodyLoadError ? "" : renderRelatedNotesPanel(entry)}
      ${entry.deferredBody && !entry.fullBodyLoaded && !entry.bodyLoadError ? "" : renderRelatedSystemsPanel(entry)}
    </section>
  `;
}

function renderSourceOutline(file, labelAnchors = new Map()) {
  const labels = file.labels || [];
  const units = file.sourceUnits || [];
  return `
    <section>
      <h3>Source Units</h3>
      ${units.length ? `<div class="compactList vertical">${units.slice(0, 40).map((unit) => `<span>${escapeHtml(unit.range)} ${escapeHtml(unit.name)}</span>`).join("")}</div>` : `<p>No source-unit comments indexed.</p>`}
    </section>
    <section>
      <h3>Labels</h3>
      ${labels.length ? `<div class="compactList vertical">${labels.slice(0, 80).map((label) => {
        const anchor = labelAnchors.get(label);
        return anchor
          ? `<button type="button" class="outlineChip" data-scroll-target="${escapeHtml(anchor)}">${escapeHtml(label)}</button>`
          : `<span>${escapeHtml(label)}</span>`;
      }).join("")}</div>` : `<p>No labels indexed.</p>`}
    </section>
  `;
}

function sourceLabelAnchorsFromCode(code) {
  const anchors = new Map();
  String(code || "").split("\n").forEach((line, index) => {
    const label = line.match(/^([A-Za-z_.$][A-Za-z0-9_.$]*):/);
    if (label && !anchors.has(label[1])) {
      anchors.set(label[1], sourceLabelAnchor(label[1], index + 1));
    }
  });
  return anchors;
}

function renderRelatedNotesPanel(entry) {
  const notes = (entry.relatedNotes || []).filter((note) => isContentVisible(entries.get(note.id))).slice(0, 12);
  if (!notes.length) {
    return "";
  }
  return `
    <section class="referenceSection">
      <h3>Related Notes</h3>
      ${renderCompactEntryList(notes.map((note) => ({ ...entries.get(note.id), matchReason: note.reason })))}
    </section>
  `;
}

function renderRelatedSystemsPanel(entry) {
  const systems = (entry.related || [])
    .map((id) => entries.get(id))
    .filter((candidate) => isContentVisible(candidate) && ["topic", "chapter", "asset-contract", "bank"].includes(candidate.kind))
    .slice(0, 10);
  if (!systems.length) {
    return "";
  }
  return `
    <section class="referenceSection">
      <h3>Related Systems</h3>
      ${renderCompactEntryList(systems)}
    </section>
  `;
}

function sourceCodeFromBody(body) {
  const match = String(body || "").match(/```(?:asm|asar)?\n([\s\S]*?)```/i);
  return match ? match[1].replace(/\n$/, "") : "";
}

function renderCompactEntryList(items) {
  const visibleItems = (items || []).filter((entry) => isContentVisible(entry));
  if (!visibleItems.length) {
    return "";
  }
  return `
    <div class="compactEntryList">
      ${visibleItems.map((entry) => `<button type="button" class="compactEntryRow" data-entry-id="${escapeHtml(entry.id)}">
        <span>${escapeHtml(entry.title)}</span>
        <small>${escapeHtml([entry.matchReason, entry.kind, entry.banks?.length ? `Bank ${entry.banks.join(", ")}` : ""].filter(Boolean).join(" - "))}</small>
      </button>`).join("")}
    </div>
  `;
}

function renderKeyValueTable(rows) {
  return `
    <table class="denseTable keyValueTable">
      <tbody>
        ${rows.map(([key, value]) => `<tr><th>${escapeHtml(key)}</th><td>${escapeHtml(value)}</td></tr>`).join("")}
      </tbody>
    </table>
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
  if (isContentVisible(entries.get(inferred))) {
    return inferred;
  }
  return (entry.related || []).find((id) => {
    const candidate = entries.get(id);
    return isContentVisible(candidate) && candidate.kind === "learning-path";
  }) || "";
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
    .filter((entry) => isContentVisible(entry) && entry.kind === "learning-path" && entry.id !== "learning-path-index" && entry.learningPath)
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
          <div class="learningList">
            ${paths.map((entry) => {
              const path = entry.learningPath || {};
              const stepCount = path.steps?.length || 0;
              const linkCount = (path.steps || []).reduce((total, step) => total + (step.items?.length || 0), 0);
              return `
                <button type="button" class="learningCard" data-entry-id="${escapeHtml(entry.id)}">
                  <span class="learningCardTitle">${escapeHtml(entry.title)}</span>
                  <span class="learningCardMeta">${stepCount} stages - ${linkCount} links${entry.banks?.length ? ` - Bank ${escapeHtml(entry.banks.slice(0, 4).join(", "))}` : ""}</span>
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
    const role = learningStepRole(step, index);
    const sectionId = uniqueHeadingId(title, headingCounts);
    currentDocumentOutline.push({ id: sectionId, level: 2, title });
    return `
      <section class="learningStep learningRole-${escapeHtml(role.id)}" id="${escapeHtml(sectionId)}">
        <div class="learningStepMarker">${index + 1}</div>
        <div class="learningStepBody">
          <div class="learningRoleLabel">${escapeHtml(role.label)}</div>
          <h2>${escapeHtml(title)}</h2>
          ${step.summary ? `<p>${escapeHtml(step.summary)}</p>` : ""}
          ${renderLearningConcepts(step.concepts || [])}
          ${renderLearningItems(step.items || [])}
          ${renderLearningTerms(step.terms || [])}
        </div>
      </section>
    `;
  }).join("");
  return `<section class="learningPathGuide">${steps}</section>`;
}

function learningStepRole(step, index) {
  const title = String(step?.title || "").toLowerCase();
  if (/narrative|start/.test(title)) return { id: "narrative", label: "Narrative" };
  if (/concept/.test(title)) return { id: "concepts", label: "Concepts" };
  if (/primary/.test(title)) return { id: "primary-evidence", label: "Primary Evidence" };
  if (/related evidence/.test(title)) return { id: "related-evidence", label: "Related Evidence" };
  if (/practical|reference/.test(title)) return { id: "practical-reference", label: "Practical Reference" };
  if (/search/.test(title)) return { id: "search-terms", label: "Search Terms" };
  if (/question|uncertain|open/.test(title)) return { id: "open-questions", label: "Open Questions" };
  return { id: index === 0 ? "narrative" : "practical-reference", label: index === 0 ? "Narrative" : "Reference" };
}

function renderLearningConcepts(concepts) {
  if (!concepts.length) {
    return "";
  }
  return `
    <div class="learningConceptList">
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
    <div class="learningList">
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
  const chapterEvidence = (entry.chapterEvidence || []).filter((item) => item.id && item.id !== entry.id && isContentVisible(entries.get(item.id)));
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
    .filter((ref) => ref.entryId && ref.entryId !== entry.id && isContentVisible(entries.get(ref.entryId)) && !chapterEvidence.some((item) => item.id === ref.entryId))
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
    .filter((ref) => ref.entryId && ref.entryId !== entry.id && isContentVisible(entries.get(ref.entryId)))
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
    .filter((id) => id !== entry.id && isContentVisible(entries.get(id)))
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
    .filter((id) => id !== entry.id && entries.has(id))
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
      return neighbor.id !== entry.id && neighborEntry && neighborEntry.kind !== "search";
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
        <h2>References</h2>
      </div>
      ${sections.join("")}
    </section>
  `;
}

function shouldShowReferenceWorkbench(entry) {
  if (entry.id === "relationship-graph" || entry.kind === "search") {
    return false;
  }
  if (entry.deferredBody && !entry.fullBodyLoaded && !entry.bodyLoadError) {
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
      <div class="referenceList">${cards.join("")}</div>
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
  const focusId = isContentVisible(entries.get(state.graphFocusId)) ? state.graphFocusId : "overview";
  const focusEntry = entries.get(focusId) || entries.get("overview");
  const hubs = (relationshipGraph.topHubs || []).filter((id) => isContentVisible(entries.get(id)));
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
  const match = normalized.match(/(?:^|\/)(notes|refs|src|tools|asset-manifests)\/(.+)$/i);
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
        <div class="deferredTitle">Full Entry</div>
        <div class="deferredText">${entry.bodyLoading ? "Loading full entry..." : `${escapeHtml(size)} available on demand.`}</div>
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

function loadDeferredData(key, chunk) {
  if (!key || !chunk) {
    return;
  }
  if (window.ENCYCLOPEDIA_DEFERRED_DATA[key]) {
    renderDocument();
    return;
  }
  const entry = entries.get(state.activeId);
  if (entry) {
    entry.dataLoading = key;
    entry.dataLoadError = "";
  }
  renderDocument();

  const script = document.createElement("script");
  script.src = chunk;
  script.onload = () => {
    if (entry) {
      entry.dataLoading = "";
      if (!window.ENCYCLOPEDIA_DEFERRED_DATA[key]) {
        entry.dataLoadError = "The generated data chunk loaded, but did not publish this table.";
      }
    }
    renderDocument();
  };
  script.onerror = () => {
    if (entry) {
      entry.dataLoading = "";
      entry.dataLoadError = "Could not load the generated data chunk.";
    }
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
    const isLongBlock = lineCount >= 36;
    const language = pre.querySelector("code")?.dataset?.language || "";
    const textLines = (pre.textContent || "").split("\n");
    const longestLine = textLines.reduce((longest, line) => Math.max(longest, line.length), 0);
    const shouldWrapByDefault = shouldWrapCodeBlockByDefault(language, longestLine);

    const wrapper = document.createElement("div");
    wrapper.className = [
      "codeBlockWrap",
      isLongBlock ? "collapsed" : "",
      shouldWrapByDefault ? "wrapCode" : ""
    ].filter(Boolean).join(" ");
    const controls = document.createElement("div");
    controls.className = "codeControls";

    if (isLongBlock) {
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
      controls.appendChild(button);
    }

    const wrapButton = document.createElement("button");
    wrapButton.className = "codeToggle";
    wrapButton.type = "button";
    wrapButton.textContent = shouldWrapByDefault ? "No wrap" : "Wrap lines";
    wrapButton.setAttribute("aria-pressed", String(shouldWrapByDefault));
    wrapButton.addEventListener("click", () => {
      const isWrapped = wrapper.classList.toggle("wrapCode");
      wrapButton.textContent = isWrapped ? "No wrap" : "Wrap lines";
      wrapButton.setAttribute("aria-pressed", String(isWrapped));
    });
    controls.appendChild(wrapButton);

    if (!isLongBlock) {
      const spacer = document.createElement("span");
      spacer.className = "codeLineCount";
      spacer.textContent = `${lineCount} lines`;
      controls.appendChild(spacer);
    }

    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(controls);
    wrapper.appendChild(pre);
  });
}

function shouldWrapCodeBlockByDefault(language, longestLine) {
  const normalized = String(language || "").toLowerCase();
  if (normalized === "msg") {
    return true;
  }
  if (normalized === "asm" || normalized === "asar" || normalized === "json") {
    return false;
  }
  return longestLine > 120;
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
    blocks.push(railBlock("Aliases", entry.aliases, { limit: 4, key: `${entry.id}:aliases` }));
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
    blocks.push(railRefBlock("Source Evidence", entry.sourceRefs, entry, { limit: 6, key: `${entry.id}:source-evidence` }));
  }
  if (entry.noteRefs && entry.noteRefs.length) {
    blocks.push(railRefBlock("Note Evidence", entry.noteRefs, entry, { limit: 6, key: `${entry.id}:note-evidence` }));
  }
  if (entry.related && entry.related.length) {
    blocks.push(railEntryBlock("Related", entry.related, entry, { limit: 6, key: `${entry.id}:related` }));
  }
  const inboundLinks = directedGraphNeighbors(entry.id, "in", 10).map((neighbor) => neighbor.id).filter((id) => id !== entry.id);
  if (inboundLinks.length) {
    blocks.push(railEntryBlock("Referenced By", inboundLinks, entry, { limit: 6, key: `${entry.id}:referenced-by` }));
  }
  const graphLinks = graphNeighbors(entry.id, 8).map((neighbor) => neighbor.id).filter((id) => id !== entry.id);
  if (graphLinks.length) {
    blocks.push(railEntryBlock("Graph Neighbors", graphLinks, entry, { limit: 6, key: `${entry.id}:graph-neighbors` }));
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
  railEl.querySelectorAll("[data-rail-toggle]").forEach((button) => {
    button.addEventListener("click", () => {
      const key = button.getAttribute("data-rail-toggle");
      state.railExpanded[key] = !state.railExpanded[key];
      renderRail(entry);
    });
  });
}

function renderFavoritesRail() {
  const favorites = state.favorites.filter((id) => isContentVisible(entries.get(id)));
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

function railBlock(title, values, options = {}) {
  const key = options.key || `${state.activeId}:${slugText(title)}`;
  const limit = options.limit || 18;
  const expanded = Boolean(state.railExpanded[key]);
  const visibleValues = expanded ? values : values.slice(0, limit);
  return `
    <section class="railBlock">
      <div class="railTitle">${escapeHtml(title)}</div>
      <div class="railList">
        ${visibleValues.map((value) => `<div class="railPill">${escapeHtml(value)}</div>`).join("")}
        ${renderRailShowToggle(key, values.length, limit, expanded)}
      </div>
    </section>
  `;
}

function railRefBlock(title, refs, entry, options = {}) {
  const filteredRefs = refs.filter((ref) => ref.entryId !== entry.id && (!ref.entryId || isContentVisible(entries.get(ref.entryId))));
  const key = options.key || `${entry.id}:${slugText(title)}`;
  const limit = options.limit || 18;
  const expanded = Boolean(state.railExpanded[key]);
  const visibleRefs = expanded ? filteredRefs : filteredRefs.slice(0, limit);
  if (!filteredRefs.length) {
    return "";
  }
  const values = visibleRefs.map((ref) => {
    const label = ref.label || ref.path;
    if (ref.entryId && entries.has(ref.entryId)) {
      return `<button type="button" class="railPill railButton" data-entry-id="${escapeHtml(ref.entryId)}">${escapeHtml(label)}</button>`;
    }
    return `<div class="railPill">${escapeHtml(label)}</div>`;
  });
  return `
    <section class="railBlock">
      <div class="railTitle">${escapeHtml(title)}</div>
      <div class="railList">${values.join("")}${renderRailShowToggle(key, filteredRefs.length, limit, expanded)}</div>
    </section>
  `;
}

function railEntryBlock(title, ids, entry, options = {}) {
  const filteredIds = ids.filter((id) => id !== entry.id && isContentVisible(entries.get(id)));
  const key = options.key || `${entry.id}:${slugText(title)}`;
  const limit = options.limit || 18;
  const expanded = Boolean(state.railExpanded[key]);
  const visibleIds = expanded ? filteredIds : filteredIds.slice(0, limit);
  if (!filteredIds.length) {
    return "";
  }
  const values = visibleIds.map((id) => {
    const entry = entries.get(id);
    const label = entry ? entry.title : id;
    return entry
      ? `<button type="button" class="railPill railButton" data-entry-id="${escapeHtml(id)}">${escapeHtml(label)}</button>`
      : `<div class="railPill">${escapeHtml(label)}</div>`;
  });
  return `
    <section class="railBlock">
      <div class="railTitle">${escapeHtml(title)}</div>
      <div class="railList">${values.join("")}${renderRailShowToggle(key, filteredIds.length, limit, expanded)}</div>
    </section>
  `;
}

function renderRailShowToggle(key, count, limit, expanded) {
  if (count <= limit) {
    return "";
  }
  return `<button type="button" class="railPill railButton railShowToggle" data-rail-toggle="${escapeHtml(key)}">${expanded ? "Show less" : `Show all ${count}`}</button>`;
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
    const label = line.match(/^([A-Za-z_.$][A-Za-z0-9_.$]*):/);
    const id = label ? ` id="${escapeHtml(sourceLabelAnchor(label[1], index + 1))}"` : "";
    return `<span class="codeLine"${id}><span class="lineText">${highlighted || " "}</span></span>`;
  }).join("");
  const languageClass = normalizedLanguage ? ` codeBlock-${escapeHtml(normalizedLanguage)}` : "";
  const languageAttribute = normalizedLanguage ? ` data-language="${escapeHtml(normalizedLanguage)}"` : "";
  return `<pre class="codeBlock codeBlockLines${languageClass}"><code${languageAttribute}>${renderedLines}</code></pre>`;
}

function sourceLabelAnchor(label, lineNumber = 0) {
  return `label-${slugText(label)}${lineNumber ? `-${lineNumber}` : ""}`;
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
    return inlinePlaceholder(index);
  });

  const escaped = escapeHtml(withMarkdownLinks)
    .replace(/`([^`]+)`/g, (_, value) => renderInlineCode(value, placeholders))
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, (_, rawId, label) => {
      const index = placeholders.length;
      const target = parseEntryTarget(rawId);
      placeholders.push(renderEntryButton(label, target));
      return inlinePlaceholder(index);
    })
    .replace(/\[\[([^\]]+)\]\]/g, (_, rawId) => {
      const index = placeholders.length;
      const target = parseEntryTarget(rawId);
      const entry = entries.get(target.id);
      placeholders.push(renderEntryButton(entry ? entry.title : target.id, target));
      return inlinePlaceholder(index);
    });

  const highlighted = semanticHighlightInline(escaped);
  return placeholders.reduce((html, value, index) => html.split(inlinePlaceholder(index)).join(value), highlighted);
}

function inlinePlaceholder(index) {
  return `%%ph${index}%%`;
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
    const index = placeholders.length;
    placeholders.push(`<code>${value}</code>`);
    return inlinePlaceholder(index);
  }
  const index = placeholders.length;
  placeholders.push(`<button type="button" class="docLink inlineCodeLink" data-entry-id="${escapeHtml(entryId)}"><code>${value}</code></button>`);
  return inlinePlaceholder(index);
}

function semanticHighlightInline(html) {
  return String(html)
    .replace(/\b((?:src|notes|refs|manifests|asset-manifests)\/[A-Za-z0-9_./-]+)/g, '<span class="semanticMark semanticPath">$1</span>')
    .replace(/\b([C-E][0-9]:[0-9A-F]{4}(?:\.\.[C-E][0-9]:[0-9A-F]{4})?|\$[0-9A-F]{4,6})\b/gi, '<span class="semanticMark semanticAddress">$1</span>')
    .replace(/\b(Bank\s+[C-E][0-9A-F]|bank-[c-e][0-9a-f])\b/gi, '<span class="semanticMark semanticBank">$1</span>')
    .replace(/\b([A-Z][A-Za-z0-9]*_[A-Za-z0-9_.$]+)\b/g, '<span class="semanticMark semanticLabel">$1</span>')
    .replace(/\b(Status|Confidence|Validated|Pending|Planned|Unsupported|Unknown|Open question|Remaining uncertainty|Build-candidate)\b/gi, '<span class="semanticMark semanticStatus">$1</span>');
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

function unique(values) {
  return [...new Set(values.filter(Boolean))];
}

function isContentVisible(entry) {
  return Boolean(entry) && !entry.metaSubject && !entry.excludeFromSearch;
}

function search(query, limit = 9, facetId = state.searchFacet || "all") {
  if (isGuideMetaQuery(query)) {
    return [];
  }
  const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
  if (!terms.length) {
    return [];
  }
  const facet = SEARCH_FACETS.find((candidate) => candidate.id === facetId) || SEARCH_FACETS[0];
  const exactSourceQuery = /^(src\/[a-z0-9/_-]+|[c-e][0-9]:[0-9a-f]{4}|\$[0-9a-f]{4,6}|[a-z_.$][a-z0-9_.$]{4,}|[a-z0-9_.-]+\.asm)$/i.test(query.trim());

  return catalog.entries
    .filter((entry) => isContentVisible(entry))
    .filter((entry) => !facet.kinds.length || facet.kinds.includes(entry.kind))
    .map((entry) => {
      const document = searchDocuments.get(entry.id);
      const haystack = document
        ? `${document.exact || ""} ${document.titleText || ""} ${document.metaText || ""} ${document.bodyText || ""}`
        : entry.searchText || "";
      const allTermsMatch = terms.every((term) => haystack.includes(term));
      let score = 0;
      const reasons = [];
      for (const term of terms) {
        if ((document?.exact || "").split(/\s+/).includes(term)) { score += 45; reasons.push("exact"); }
        if ((document?.titleText || entry.title.toLowerCase()).includes(term)) { score += 18; reasons.push("title"); }
        if (entry.title.toLowerCase().startsWith(term)) score += 18;
        if (entry.kind.toLowerCase() === term) { score += 35; reasons.push("kind"); }
        if ((document?.metaText || "").includes(term)) { score += 8; reasons.push(matchReasonForTerm(entry, document, term)); }
        if ((document?.bodyText || "").includes(term)) { score += 2; reasons.push("body/comment"); }
        if (!document && haystack.includes(term)) { score += 1; reasons.push("body"); }
      }
      if (allTermsMatch) score += 10;
      if (exactSourceQuery && ["source", "source-file", "symbol", "routine", "bank"].includes(entry.kind)) {
        score += 30;
      }
      return { entry, score, allTermsMatch, reason: unique(reasons).slice(0, 3).join(" / ") };
    })
    .filter((result) => result.score > 0 && (result.allTermsMatch || exactSourceQuery))
    .sort((a, b) => b.score - a.score || a.entry.title.localeCompare(b.entry.title))
    .slice(0, limit === Infinity ? undefined : limit);
}

function isGuideMetaQuery(query) {
  return /^(public\s+(status\s+)?truthfulness|release\s+(readiness|checklist|artifact|policy)|catalog\s+build(\s+status)?|project\s+status|source\s+readiness)$/i.test(String(query || "").trim());
}

function matchReasonForTerm(entry, document, term) {
  if ((entry.sourceFile?.path || "").toLowerCase().includes(term)) return "path";
  if ((entry.sourceFile?.labels || []).some((label) => label.toLowerCase().includes(term))) return "label";
  if ((entry.addresses || []).some((address) => address.toLowerCase().includes(term))) return "address";
  if ((entry.banks || []).some((bank) => bank.toLowerCase().includes(term))) return "bank";
  if ((document?.metaText || "").includes(term)) return "metadata";
  return "match";
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
  const totalByFacet = SEARCH_FACETS.map((facet) => ({
    ...facet,
    count: facet.id === "all"
      ? search(searchInput.value, Infinity, "all").length
      : search(searchInput.value, Infinity, facet.id).length
  }));
  searchResults.innerHTML = [
    `<div class="searchFacetBar">
      ${totalByFacet.map((facet) => `<button type="button" class="searchFacet${facet.id === state.searchFacet ? " active" : ""}" data-search-facet="${escapeHtml(facet.id)}">${escapeHtml(facet.label)} <span>${Number(facet.count).toLocaleString()}</span></button>`).join("")}
    </div>`,
    ...results.map(({ entry, reason }, index) => `
      <button type="button" class="searchItem${index === searchSelectionIndex ? " active" : ""}" data-entry-id="${escapeHtml(entry.id)}" data-search-index="${index}" aria-selected="${index === searchSelectionIndex ? "true" : "false"}">
        <div class="searchItemTitle">${escapeHtml(entry.title)}</div>
        <div class="searchItemMeta">${escapeHtml([displayKindLabel(entry), entry.banks && entry.banks.length ? `Bank ${entry.banks.join(", ")}` : "", reason ? `matched ${reason}` : ""].filter(Boolean).join(" - "))}</div>
      </button>
    `),
    `<button type="button" class="searchItem${searchSelectionIndex === results.length ? " active" : ""}" data-entry-id="${fullResultsId}" data-search-index="${results.length}" aria-selected="${searchSelectionIndex === results.length ? "true" : "false"}">
      <div class="searchItemTitle">Open full search results</div>
      <div class="searchItemMeta">View linked result set in a tab</div>
    </button>`
  ].join("");

  const resultEntry = entries.get(fullResultsId);
  if (resultEntry) {
    const fullResults = search(searchInput.value, FULL_RESULTS_LIMIT, state.searchFacet);
    const grouped = new Map();
    for (const result of fullResults) {
      grouped.set(result.entry.kind, [...(grouped.get(result.entry.kind) || []), result]);
    }
    const totalMatches = search(searchInput.value, Infinity, state.searchFacet).length;
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
      `## ${displayKindLabel({ kind })}`,
      group.map(({ entry, reason }) => `- [[${entry.id}|${entry.title}]] - ${[displayKindLabel(entry), reason ? `matched ${reason}` : "", entry.summary || entry.kind].filter(Boolean).join("; ")}`).join("\n")
      ].join("\n"))
    ].join("\n\n");
  }

  searchResults.querySelectorAll("[data-search-facet]").forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      state.searchFacet = button.getAttribute("data-search-facet") || "all";
      searchSelectionIndex = 0;
      renderSearchResults(search(searchInput.value, 9, state.searchFacet));
    });
  });
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

function displayKindLabel(entry) {
  const kind = typeof entry === "string" ? entry : entry?.kind || "";
  const text = typeof entry === "object"
    ? `${entry.title || ""} ${entry.summary || ""} ${(entry.aliases || []).join(" ")}`.toLowerCase()
    : "";
  if (/(^|\b)(asset|sprite|graphics|palette|manifest|data contract|contract)(\b|$)/.test(text)) {
    if (/data contract|contract/.test(text)) {
      return "Data contract";
    }
    if (/manifest|asset|sprite|graphics|palette/.test(text)) {
      return "Manifest documentation";
    }
  }
  const labels = {
    "asset": "Manifest documentation",
    "asset-contract": "Data contract",
    "asset-manifest": "Manifest documentation",
    "bank": "Bank",
    "chapter": "Chapter",
    "learning-path": "Learning path",
    "narrative": "Narrative chapter",
    "note": "Note",
    "reference-document": "Reference document",
    "reference-script": "MSG reference",
    "reference-source": "Reference source",
    "reference-table": "Reference table",
    "routine": "Routine",
    "script-vm": "Script VM",
    "search": "Search",
    "source": "Source index",
    "source-file": "Source file",
    "symbol": "Symbol",
    "text-command": "Text command",
    "tool": "Tool notes",
    "topic": "System topic",
    "workflow": "Validation/workflow"
  };
  return labels[kind] || kind;
}

searchInput.addEventListener("input", (event) => {
  searchSelectionIndex = 0;
  renderSearchResults(search(event.target.value, 9, state.searchFacet));
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
    renderSearchResults(search(searchInput.value, 9, state.searchFacet));
  } else if (event.key === "ArrowUp") {
    event.preventDefault();
    searchSelectionIndex = (searchSelectionIndex - 1 + currentSearchResults.length) % currentSearchResults.length;
    renderSearchResults(search(searchInput.value, 9, state.searchFacet));
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
  renderBuildStatusButton();
}

function renderBuildStatusButton() {
  if (!buildStatusButton) {
    return;
  }
  const mode = catalog.buildMode || "local";
  const label = mode === "authored" ? "Authored" : mode === "private" ? "Private" : "Local";
  const target = mode === "private" && entries.has("reference-snapshot") ? "reference-snapshot" : "catalog-build-status";
  buildStatusButton.textContent = `${label} catalog`;
  buildStatusButton.dataset.entryId = target;
  buildStatusButton.classList.toggle("local", mode !== "authored");
  buildStatusButton.title = mode === "private"
    ? "Private bundled reference catalog. Open build status."
    : mode === "authored"
    ? "Authored release baseline. Open release artifact policy."
    : "Local generated catalog. Open ROM and generated content status.";
}

backButton.addEventListener("click", goBack);
forwardButton.addEventListener("click", goForward);
if (buildStatusButton) {
  buildStatusButton.addEventListener("click", () => {
    const target = buildStatusButton.dataset.entryId || "release-artifact-policy";
    openEntry(entries.has(target) ? target : "overview");
  });
}

render();
