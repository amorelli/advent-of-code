const { input } = require("./input.js");
console.time("f");
// console.log(input);

// const data = String(input).split(/(?<!.)\n/);
const data = input.split("\n");

console.log(data);

let accumulate = 0;
const vals = [];

for (let i = 0; i < data.length; i++) {
  if (data[i] === "") {
    vals.push(accumulate);
    accumulate = 0;
  } else {
    accumulate = accumulate + Number(data[i]);
  }
  console.log(data[i], ": ", "accumulate: ", accumulate);
  console.log("------");
}

const sum = vals
  .sort((a, b) => b - a)
  .slice(0, 3)
  .reduce((a, b) => a + b, 0);
console.log("sum: ", sum);
console.log("actual: ", 70369 + 66781 + 65852);
console.timeEnd("f");
return sum;
