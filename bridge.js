window.addEventListener("message", async (e) => {
  if (e.source !== window || !e.data || e.data.type !== "OSM_PINS_REQUEST") return;

  let pins = [];
  try {
    const res = await chrome.runtime.sendMessage({ type: "getPins" });
    pins = res.pins || [];
  } catch (err) {
    console.warn("Server not reacheble", err);
  }

  window.postMessage({ type: "OSM_PINS_RESPONSE", id: e.data.id, pins }, "*");
});