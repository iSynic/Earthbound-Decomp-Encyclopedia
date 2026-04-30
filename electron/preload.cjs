const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("earthboundWorkspace", {
  selectRom: () => ipcRenderer.invoke("workspace:select-rom"),
  openFolder: (folderPath) => ipcRenderer.invoke("workspace:open-folder", folderPath),
  generateFamily: (workspaceRoot, familyId) => ipcRenderer.invoke("workspace:generate-family", workspaceRoot, familyId),
  generateAll: (workspaceRoot) => ipcRenderer.invoke("workspace:generate-all", workspaceRoot),
  exportFamily: (workspaceRoot, familyId) => ipcRenderer.invoke("workspace:export-family", workspaceRoot, familyId),
  exportAll: (workspaceRoot) => ipcRenderer.invoke("workspace:export-all", workspaceRoot),
  readFile: (workspaceRoot, familyId, relativePath) => ipcRenderer.invoke("workspace:read-file", workspaceRoot, familyId, relativePath),
  readMedia: (workspaceRoot, familyId, relativePath) => ipcRenderer.invoke("workspace:read-media", workspaceRoot, familyId, relativePath)
});
