function cube (num) {
    return num*num*num;
}
console.log(cube(3));

function sumOfCubes (num1, num2) {

    return num1*num1*num1 + num2*num2*num2;
}
console.log(sumOfCubes(5,6));

function countE() {
    var phrase = prompt("Please give me a phrase to check for e's!");
    if (typeof(phrase) != "string") {
        alert("That's not a valid entry!");
        return false;
    } else {
        var eCount = 0;
        for (var i = 0; i < phrase.length; i++) {
            if (phrase[i] === "e" || phrase[i] === "E")
                eCount++;
        }
    }
    alert("There are " + eCount + " e's in \"" + phrase + "\".");
    console.log(eCount);
    return 0;
}
countE();