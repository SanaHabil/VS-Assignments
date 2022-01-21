function reverse(arr) {
    // your code here
    var reversedArr = [];
    for(i=(arr.length-1); i>=0; i--){
        reversedArr.push(arr[i]);
    }
    arr = reversedArr;
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]
