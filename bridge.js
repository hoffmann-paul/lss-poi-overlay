window.addEventListener("message", async (e) => {

    if (
        e.source !== window ||
        !e.data ||
        e.data.type !== "OSM_PINS_REQUEST"
    ) return;

    let pins = [];

    try {

        const res = await chrome.runtime.sendMessage({
            type: "getPins",
            city: e.data.city
        });

        pins = res.pins || [];

    } catch (err) {

        console.warn("Server not reachable", err);

    }

    window.postMessage({
        type: "OSM_PINS_RESPONSE",
        id: e.data.id,
        pins: pins
    }, "*");

});