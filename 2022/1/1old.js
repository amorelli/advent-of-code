const { input } = require("./input.js");
console.time("f");
// console.log(input);

// const data = String(input).split(/(?<!.)\n/);
const data = input.split("\n");

console.log(data);

let largest = 0;
let compare = 0;

for (let i = 0; i < data.length; i++) {
  if (data[i] === "") {
    if (compare > largest) {
      largest = compare;
    }
    compare = 0;
  } else {
    compare = compare + Number(data[i]);
  }
  console.log(data[i], ": ", "largest: ", largest, "compare: ", compare);
  console.log("------");
}
console.log("largest is: ", largest);
console.timeEnd("f");
return largest;
