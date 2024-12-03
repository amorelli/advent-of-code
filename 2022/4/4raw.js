const { input } = require("./input.js");
console.time("f");
const data = input.split("\n");

let p1Sum = 0;
let p2Sum = 0;

for (let i = 0; i < data.length; i++) {
  const secOne = Number(data[i].match(/^\d*(?=-)/)[0]);
  const secTwo = Number(data[i].match(/(?<=-)\d*/)[0]);
  const secThree = Number(data[i].match(/(?<=,)\d*/)[0]);
  const secFour = Number(data[i].match(/\d*$/)[0]);

  if (
    (secOne <= secThree && secTwo >= secFour) ||
    (secThree <= secOne && secFour >= secTwo)
  ) {
    p1Sum += 1;
  }

  if (
    (secOne <= secFour && secOne >= secThree) ||
    (secTwo >= secThree && secTwo <= secFour) ||
    (secThree >= secOne && secThree <= secTwo) ||
    (secFour >= secOne && secFour <= secTwo)
  ) {
    p2Sum += 1;
  }
}

console.log("Problem 1:", p1Sum);
console.log("Problem 2: ", p2Sum);

console.timeEnd("f");
