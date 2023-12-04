'use strict';

async function fetchJoke(){
    try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const joke = await response.json();
    console.log(joke.value);
    } catch(error) {
        console.log('fetch error', error);
    }
}

fetchJoke();