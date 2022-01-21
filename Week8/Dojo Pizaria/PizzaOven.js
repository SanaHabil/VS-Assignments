/*
var pizza = {
    crustType:    "thin",
    souceType:  "white",
    cheeses:   ["mozzrila"],
    toppings: ["mashroms", "spinitch", "onions"]
};
*/    
//console.log(pizza);


function pizzaOven(crustType, souceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.souceType = souceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}
  
var s1 = pizzaOven("thin", "white", "mozzrila", ["mashroms", "spinitch", "onions"]);
console.log(s1);
var s2 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepproni", "susage"]);
console.log(s2);

var s3 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"],["mushrooms", "olives", "onions"]);
console.log(s3);
var s4 = pizzaOven("thin", "marinara", ["parmasian", "gooda"],["olives", "green pepper", "salami"]);
console.log(s4);

var s5 = pizzaOven("deep dish", "basile", ["chedar", "fresh mozzarella"],["pickles", "pepper"]);
console.log(s5);
var s6 = pizzaOven("new york style", "ranch", ["mozzarella", "smoked gooda"],["ham", "olives", "pinapples"]);
console.log(s6);


// first function to solve the problem (built an array of ready pizzas)
var pizzas = [s1, s2, s3, s4, s5, s6];
function randomPizza(){
    var pizzaNum = Math.floor(Math.random()*(pizzas.length-1));
    var pizzaChoice = pizzas[pizzaNum];
    return pizzaChoice;
    
}

var result = randomPizza();
console.log(result);

// second function to solve the problem
var crustTypes = [
    "thin",
    "deep dish" ,
    "glutin free",
    "tradetional",
    "stuffed edges"
];
var souceTypes = [
    "marinara",
    "pesto",
    "white",
    "bbq"
];
var cheeses = [
    "mozarrela",
    "cheddar",
    "feta",
    "parmesan"
];
var toppings = [
    "onions",
    "green peppers",
    "mashrooms",
    "pinapples",
];

function range(max, min){
    return Math.floor(Math.random()* max-min)+ min;

}


console.log(range(4,1));

function pickValue(arr){
    var i = Math.floor(arr.length * Math.random());
    return arr[i];
}
function MakeRandomPizza(){
    var pizza = {};
    pizza.crustType = pickValue(crustTypes);
    //console.log(pizza.crustType);
    pizza.souceType = pickValue(souceTypes);
    pizza.cheeses = [];
    for(var i=0; i< range(4,1); i++){
        pizza.cheeses.push(pickValue(cheeses));
    }
    pizza.toppings = [];
    for(var i=0; i< range(4,1); i++){
        pizza.toppings.push(pickValue(toppings));
    }
    return pizza;

}

var result = MakeRandomPizza();
console.log(result);