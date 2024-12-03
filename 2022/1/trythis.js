const { input } = require("./input.js");

console.time("Function #1");
let arrayfy = input.split("\n");
let accumulator = 0;
let arrayOfCalories = [];
for (let i = 0; i < arrayfy.length; i++) {
  if (arrayfy[i] !== "") {
    accumulator += Number(arrayfy[i]);
  } else {
    arrayOfCalories.push(accumulator);
    accumulator = 0;
  }
}

let sortedArray = arrayOfCalories.sort((a, b) => b - a);
console.log(sortedArray[0] + sortedArray[1] + sortedArray[2]);
console.timeEnd("Function #1");
