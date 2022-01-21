function displayIfChildIsAbleToRideTheRollerCoaster(childHeight){
    if(childHeight > 52){
       return console.log("Get on that ride, kiddo!");
    } else {
       return console.log("Sorry kiddo. Maybe next year.");
    }

}
var childHeight = 78;
displayIfChildIsAbleToRideTheRollerCoaster(childHeight)