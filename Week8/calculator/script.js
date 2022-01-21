var displayDiv = document.querySelector("#display");
displayDiv.innerText = "Some new value";

var pressedBTN = false;
function press(element){
    pressedBTN = true;
    displayDiv.innerText = element;
    console.log(displayDiv.innerText);
}

if(pressedBTN){
    var num = displayDiv.innerText;
}

function setOP(element){
    if(element == "+"){
        num += num;
    } else if(element == "-"){
        displayDiv -= press(element);
        displayDiv.innerText = displayDiv;
    } else if(element == "*"){
        displayDiv *= press(element);
        displayDiv.innerText = displayDiv;
    } else if(element == "/"){
        displayDiv /= press(element);
        displayDiv.innerText = displayDiv;
    }
    return num;
}

function calculate(){
        setOP();
}
    