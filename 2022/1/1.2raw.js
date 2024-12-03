const { input } = require("./input.js");
const data = input.split("\n");

let accumulate = 0;
const vals = [];

for (let i = 0; i < data.length; i++) {
  if (data[i] === "") {
    vals.push(accumulate);
    accumulate = 0;
  } else {
    accumulate = accumulate + Number(data[i]);
  }
}

const sum = vals
  .sort((a, b) => b - a)
  .slice(0, 3)
  .reduce((a, b) => a + b, 0);

console.log("Highest cals: ", vals[0]);
console.log("Sum of 3 highest: ", sum);

return sum;
