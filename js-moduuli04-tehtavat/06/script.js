'use strict';


async function getJokes(){
    try{
        const qElem = document.querySelector('input[name="query"]').value;
        const response = await fetch('https://api.chucknorris.io/jokes/search?query=' + qElem);
        const jokes = await response.json();
        return jokes;
    }catch(error){
        console.log('fetch error', error);
        return null;
    }
}

function clearThePage(){
    const existingArticles = document.querySelectorAll('article');
    existingArticles.forEach(article => article.remove());
}

async function showJoke(){
    const jokes = await getJokes();
    clearThePage();
    console.log(jokes);
    if (jokes !== null){
        try {
            for (let i = 0; i < jokes.result.length; i++){
                const jokeElem = document.createElement('p');
                const article = document.createElement('article');

                jokeElem.innerHTML = `${i + 1}. ${jokes.result[i].value}`;

                article.append(jokeElem);
                document.querySelector('body').append(article);
            }
        }catch(error){
            console.log('fetch error', error);
        }
    }
}


document.querySelector('input[type="submit"]').addEventListener('click', function(event){
    event.preventDefault();
    showJoke();
});