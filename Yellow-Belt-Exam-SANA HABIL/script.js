console.log("page loaded...");

function msg(){
    alert("This game is suppored on Linux");
}

var items = document.querySelector("#shopping-items").innerText;
//console.log(items);
function addToCart(){
    items++;
    document.querySelector("#shopping-items").innerText = items;
}

var newImg = document.querySelector("#current-img");
function imgChange(){
    newImg.src = "images/pixel-ninjas-2.png";
}

var oldImg = document.querySelector("#current-img");
function changeImgBack(){
    oldImg.src = "images/stonepunk.png"
}