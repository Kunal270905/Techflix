let map;
let directionsService;
let directionsRenderer;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 12.9716, lng: 77.5946 },
        zoom: 12,
    });

    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);
}

window.onload = initMap;

async function findRoutes() {
    const source = document.getElementById("source").value;
    const destination = document.getElementById("destination").value;
    const time = document.getElementById("time").value;

    const res = await fetch("http://127.0.0.1:5000/api/routes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ source, destination, time })
    });

    const data = await res.json();
    showRoutes(data.all_routes);

    drawRoute(source, destination);

    speak(data.best_route.route + " is the best route");
}

function drawRoute(source, destination) {
    directionsService.route({
        origin: source,
        destination: destination,
        travelMode: "DRIVING"
    }, (result, status) => {
        if (status === "OK") {
            directionsRenderer.setDirections(result);
        }
    });
}

function showRoutes(routes) {
    const container = document.getElementById("routes");
    container.innerHTML = "";

    routes.forEach((r, i) => {
        const div = document.createElement("div");
        div.className = "route-card";

        div.innerHTML = `
      <h3>${r.route} ${i === 0 ? "🏆 Best" : ""}</h3>
      <p>⏱ ${r.time} mins</p>
      <p>🚗 Traffic: ${r.traffic}</p>
      <p>🛡 Score: ${r.final_score}</p>
      <p>${r.advice}</p>
    `;

        container.appendChild(div);
    });
}

function speak(text) {
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US";
    window.speechSynthesis.speak(speech);
}