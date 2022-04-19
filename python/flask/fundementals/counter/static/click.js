var num1 = document.querySelector("#like-num")
var num2 = document.querySelector("#like-num")
var num3 = document.querySelector("#like-num")
var num4 = document.querySelector("#like-num")

var likes_counter = {{ session['click'] }}

function addLikes1(){
        likes_counter++
        num1.innerText = likes_counter + ''
        }  

function addLikes2(){
        likes_counter++
        num2.innerText = ' '
        }
function addLikes3(){
        likes_counter += 2
        num3.innerText = likes_counter + ''
        }  

function addLikes4(){
        likes_counter = likes_counter + {{ inc }}
        num4.innerText = ' '
        }        