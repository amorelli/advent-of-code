/*
 * X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
 */

const { input } = require("./input.js");
console.time("f");
const data = input.split("\n");

const lookup = {
  // opponent rock
  A: {
    X: 3, // lose
    Y: 4, // draw
    Z: 8 // win
  },
  // opponent paper
  B: {
    X: 1,
    Y: 5,
    Z: 9
  },
  // opponent scissors
  C: {
    X: 2,
    Y: 6,
    Z: 7
  }
};

const getSum = () => {
  let sum = 0;

  data.forEach(pair => {
    let one = pair.slice(0, 1);
    let two = pair.slice(2);
    const score = lookup[one][two];
    sum = sum + score;
    return score;
  });

  return sum;
};

console.log(getSum());

console.timeEnd("f");
