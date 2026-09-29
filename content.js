function requestPins() {
  return new Promise((resolve) => {
    const id = Math.random().toString(36).slice(2);
    function onMsg(e) {
      if (e.source !== window || !e.data) return;
      if (e.data.type !== "OSM_PINS_RESPONSE" || e.data.id !== id) return;
      window.removeEventListener("message", onMsg);
      resolve(e.data.pins || []);
    }
    window.addEventListener("message", onMsg);
    window.postMessage({ type: "OSM_PINS_REQUEST", id }, "*");
  });
}

async function addPins(map) {
  const pins = await requestPins();
  const icon = L.divIcon({
    className: "",
    html: '<div style="font-size:28px;transform:translate(-50%,-100%)">📍</div>',
    iconSize: [0, 0],
  });
  pins.forEach((p) => {
    L.marker([p.lat, p.lng], { icon }).addTo(map).bindPopup(p.label);
  });
}

function hookLeaflet(L) {
  if (L.__pinsHooked) return;
  L.__pinsHooked = true;
  L.Map.addInitHook(function () {
    const map = this;
    map.whenReady(() => addPins(map));
  });
}

if (window.L && window.L.Map) {
  hookLeaflet(window.L);
} else {
  let _L;
  Object.defineProperty(window, "L", {
    configurable: true,
    get() { return _L; },
    set(v) {
      _L = v;
      if (v && v.Map) hookLeaflet(v);
    },
  });
}