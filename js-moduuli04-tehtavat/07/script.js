'use strict';

const map = L.map('map').setView([60.1695, 24.9354], 13); // Use the coordinates of your desired map center
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);


// Example query for bus stops in Helsinki
const query = `
    {
        stops(name: "Helsinki") {
            name
            lat
            lon
        }
    }
`;

async function fetchData() {
    try {
        const response = await fetch(`https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql/YOUR_DIGITRANSIT_API_KEY`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query })
        });

        const data = await response.json();

        // Process the data and add markers to the map
        data.data.stops.forEach(stop => {
            L.marker([stop.lat, stop.lon]).addTo(map)
                .bindPopup(stop.name);
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Call the fetchData function
fetchData();