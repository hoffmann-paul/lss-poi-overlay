document.getElementById("button").addEventListener("click", () => {
    const name = document.getElementById("name").value;

    document.getElementById("output").textContent =
        "Hallo " + name + "!";
});