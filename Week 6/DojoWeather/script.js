function hide(){
    var element = document.querySelector("#alert-cookie");
    element.remove();
}

// copied from the solution/ I wasn't able to get it right.
function c2f(temp) {
    return Math.round(9 / 5 * temp + 32);
}

function f2c(temp) {
    return Math.round(5 / 9 * (temp - 32));
}

function convert(element){
    console.log(element.value);
    for(var i=1; i<9; i++) {
        var tempSpan = document.querySelector("#num" + i);
        console.log(tempSpan);
        var tempVal = parseInt(tempSpan.innerText);
        if(element.value == "°C") {
            tempSpan.innerText = f2c(tempVal)+ "°";
        } else {
            tempSpan.innerText = c2f(tempVal)+ "°";
        }
    }
}    