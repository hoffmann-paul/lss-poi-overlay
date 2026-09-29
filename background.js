chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === "getPins") {
    fetch("http://127.0.0.1:8765/pins")
      .then((r) => r.json())
      .then((pins) => sendResponse({ pins }))
      .catch((err) => sendResponse({ pins: [], error: String(err) }));
    return true; 
  }
});