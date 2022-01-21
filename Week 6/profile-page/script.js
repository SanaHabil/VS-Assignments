console.log("page loaded...");

function hide(){

    var user = document.querySelector(".card-list-item")
    user.remove();
    document.querySelector(".badge").innerText--;
    
}
function addConnection(){

    document.querySelector(".badge").innerText++;
    
}
function changeName(){
    var newusername = "Sana Habil";
    var username = document.querySelector("#usern");
    username.innerText = newusername;

}