
var num1 = document.querySelector("#card-1")
var num2 = document.querySelector("#card-2")
var num3 = document.querySelector("#card-3")
var likes_counter = 0;

function addLikes1(){
        likes_counter++
        num1.innerText = likes_counter + "  Like(s)"
        }  

function addLikes2(){
        likes_counter++
        num2.innerText = likes_counter + "  Like(s)"
        }
function addLikes3(){
        likes_counter++
        num3.innerText = likes_counter + "  Like(s)"
        }  
    