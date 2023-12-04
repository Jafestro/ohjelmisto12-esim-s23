async function fetchLentokentta(icaoCode){
    let nimi, icao, municipality;
    try {
        const response = await fetch('http://localhost:3000/lentokentta/' + icaoCode);
        const lentokentta = await response.json();
        console.log('moderni async vitsi', lentokentta);
        nimi = lentokentta.Name;
        icao = lentokentta.ICAO;
        municipality = lentokentta.Municipality;
    } catch(error) {
        console.log('fetch error', error);
        const joke = {};
        jokeContent = "You are a joke";
    }
    document.querySelector('#toka').textContent = `${nimi} ${icao} ${municipality}`;
}
const icao = prompt('Antaa lentokentan icao koodi');
fetchLentokentta(icao);