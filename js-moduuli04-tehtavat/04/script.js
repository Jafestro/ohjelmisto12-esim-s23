'use strict';

async function getShow(){
    try{
        const qElem = document.querySelector('input[name="q"]').value;
        const response = await fetch('https://api.tvmaze.com/search/shows?q=' + qElem);
        const show = await response.json();
        return show;
    }catch(error){
        console.log('fetch error', error);
        return null;
    }
}

function clearThePage(){
    const existingArticles = document.querySelectorAll('article');
    existingArticles.forEach(article => article.remove());
}

async function getShowArticle(){
    const show = await getShow();
    clearThePage();
    console.log(show);
    if (show !== null){
        try {
            const article = document.createElement('article');
            for (let i = 0; i < show.length; i++){
                const nameElem = document.createElement('h2');
                const linkElem = document.createElement('a');
                const imgElem = document.createElement('img');
                const summaryElem = document.createElement('div');

                nameElem.innerHTML = show[i].show.name;

                linkElem.target = "_blank";
                linkElem.href = show[i].show.officialSite;
                
                if(show[i].show.image?.medium !== undefined)
                    imgElem.src = show[i].show.image.medium;
                else
                    imgElem.src = "https://via.placeholder.com/210x295?text=Not%20Found";
                imgElem.alt = show[i].show.name;

                summaryElem.innerHTML = show[i].show.summary;

                article.append(nameElem);
                article.append(linkElem);
                article.append(imgElem);
                article.append(summaryElem);
            }
            document.querySelector('body').append(article);
        }catch(error){
            console.log('fetch error', error);
        }
    }
}


document.querySelector('input[type="submit"]').addEventListener('click', function(event){
    event.preventDefault();
    getShowArticle();
});
