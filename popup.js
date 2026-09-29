async function loadPins(city) {

    try {

        const res = await chrome.runtime.sendMessage({
            type: "getPins",
            city: city
        });

        const pins = res.pins || [];

        reloadMap(pins);

    } catch (err) {

        console.error("Pins konnten nicht geladen werden:", err);

    }
}


document.getElementById("button").addEventListener("click", () => {

    const frontend_city = document.getElementById("city").value;

    loadPins(frontend_city);

});