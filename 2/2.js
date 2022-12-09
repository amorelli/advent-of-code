const { input } = require("./input.js");
console.time("f");
const data = input.split("\n");

const lookup = {
  // opponent rock
  A: {
    X: 4, // rock
    Y: 8, // paper
    Z: 3 // scissors
  },
  // opponent paper
  B: {
    X: 1,
    Y: 5,
    Z: 9
  },
  // opponent scissors
  C: {
    X: 7,
    Y: 2,
    Z: 6
  }
};

const lookup2 = {
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

const getSum = table => {
  let sum = 0;

  data.forEach(pair => {
    let one = pair.slice(0, 1);
    let two = pair.slice(2);
    const score = table[one][two];
    sum = sum + score;
    return score;
  });

  return sum;
};

console.log("Part 1 total: ", getSum(lookup));
console.log("Part 2 total: ", getSum(lookup2));

console.timeEnd("f");
