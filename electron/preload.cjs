const { contextBridge } = require("electron");

contextBridge.exposeInMainWorld("earthboundWorkspace", {
  privateReference: true
});
