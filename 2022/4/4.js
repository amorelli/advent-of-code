const { input } = require("./input.js");
console.time("f");
const data = input.split("\n");

let p1Sum = 0;
let p2Sum = 0;

const range = (from, to) =>
  Array.from(new Array(to + 1), (x, i) => i).splice(from);

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

  const groupOneNodes = range(secOne, secTwo);
  const groupTwoNodes = range(secThree, secFour);

  if (groupOneNodes.filter(x => groupTwoNodes.includes(x)).length > 0) {
    p2Sum += 1;
  }
}

console.log("Problem 1:", p1Sum);
console.log("Problem 2: ", p2Sum);

console.timeEnd("f");
