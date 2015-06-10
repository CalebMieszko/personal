var passengers = ["Greg Pollack", "Aimee Simone", "Thomas Meeks", "Olivier Lacan", "Jon Friskics", "Ashely Smith"];
var comboArray1 = ["One", "fish", 2, "fish"];
var poisson = "fish";
var comboArray2 = ["Red", poisson, "Blue", poisson];
var arrayOfArrays = [comboArray1, comboArray2];
var numberList = [2, 5, 8, 4, 7, 12, 6, 9, 2, 11];
var passengerList = [];

function log(content){
    console.log(content);
}

log("Initial list: " + passengers + "\n");

passengers[2] = "Eric Allam" + "\n";
log("Thomas becomes Eric: " + passengers + "\n");

passengers.pop();
log("Popped list: " + passengers + "\n");

passengers.push("Adam Rensel");
log("Adam pushed: " + passengers + "\n");

log("Array of arrays: " + arrayOfArrays + "\n")

log("Testing requesting data from arrays contained within arrayOfArrays: \n")
console.log(arrayOfArrays[0]);
console.log(arrayOfArrays[1]);
console.log(arrayOfArrays[0][3]);
console.log(arrayOfArrays[1][3]);
console.log("\n");

function evenNumbers(array) {
    log("Here is the current state of the array: " + array);
    var evenCount = 0;
    for (var i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0) {
            evenCount++;
        } else {
            array[i] = undefined;
        }
    }
    log("Testing evenNumbers function: " + evenCount + "\nAnd here is the array now: " + array + "\n");

}
evenNumbers(numberList);

function addPassenger (passengerName, list){
    if (list.length === 0) {
        list.push(passengerName);
    } else {
        for (i = 0; i < list.length; i++) {
            if (list[i] === undefined){
                list[i] = passengerName;
                return list;
            } else if (i === list.length - 1) {
                list.push(passengerName);
                return list;
            }
        }
    }
    log("Testing addPassenger: " + passengerList);
}

log("Adding passengers to list: ");
passengerList = addPassenger("Greg Pollock", passengerList);
passengerList = addPassenger("Ashley Smith", passengerList);
passengerList = addPassenger("John Friskics", passengerList);
log(passengerList);