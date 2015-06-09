 var fizzBuzz = function() {
     for (var i = 1; i <= 100; i++) {
         var output = "";

         if (i % 3 === 0) {
             output += "Fizz";
         }
         if (i % 5 === 0) {
             output += "Buzz";
         }
         if (output === "") {
             continue;
         }
         console.log(output);
     }
     return 0;
 };

 fizzBuzz();