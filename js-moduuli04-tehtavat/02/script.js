'use strict';

async function getShow(){
    try{
        const qElem = document.querySelector('input[name="q"]').value;
        const response = await fetch('https://api.tvmaze.com/search/shows?q=' + qElem);
        const show = await response.json();
        console.log(show);
    }catch(error){
        console.log('fetch error', error);
    }
}


document.querySelector('input[type="submit"]').addEventListener('click', function(event){
    event.preventDefault();
    getShow();
});
