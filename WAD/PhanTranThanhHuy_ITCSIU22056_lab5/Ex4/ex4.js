function updateWords() {
    const words = document.querySelector(".input-box").value;
    
    let countWords = '';
    countWords = `${words.length}/250`;

    if(words.length > 250){
        document.querySelector(".input-box").classList.add("input-box-alert");
        document.querySelector(".words").classList.add("words-alert");
    }
    else{
        document.querySelector(".input-box").classList.remove("input-box-alert");
        document.querySelector(".words").classList.remove("words-alert");
    }

    if(!countWords)
        countWords = '0/250';

    document.querySelector(".words").innerHTML = countWords;
}

setInterval(() => {
    updateWords();
},100);

