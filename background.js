chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    if (message.type !== "getPins") {
        return;
    }

    const city = message.city || "stuttgart";

    const url =
        "http://127.0.0.1:8765/pins?city=" +
        encodeURIComponent(city);

    fetch(url)
        .then(response => {

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            return response.json();

        })
        .then(pins => {

            sendResponse({
                pins: pins
            });

        })
        .catch(error => {

            console.error("Python server error:", error);

            sendResponse({
                pins: []
            });

        });

    return true;
});