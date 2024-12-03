// Rock = A,X
// Paper = B,Y
// Scissors = C,Z
// Rock > Scissors, Scissors > Paper, and Paper > Rock

// const { input } = require("./input.js");
const input = `A Y
B X
C Z`;

console.time("f");
const data = input.split("\n");
console.log(data);

/* The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won) */

const lookup = {
  rock: {
    rock: 4,
    paper: 1,
    scissors: 7
  },
  paper: {
    rock: 8,
    paper: 5,
    scissors: 2
  },
  scissors: {
    rock: 8,
    paper: 5,
    scissors: 2
  }
};

const getScore = (hand1, hand2) => {
  hand1 = normalizeInput(hand1);
  hand2 = normalizeInput(hand2);
  console.log(hand1, hand2, lookup[hand2][hand1]);
  return lookup[hand2][hand1];
};

const normalizeInput = input => {
  if (["A", "X"].includes(input)) {
    return "rock";
  }
  if (["B", "Y"].includes(input)) {
    return "paper";
  }
  return "scissors";
};

let sum = 0;

data.forEach(pair => {
  let one = pair.slice(0, 1);
  let two = pair.slice(2);
  const score = getScore(one, two);
  sum = sum + score;
  return score;
});

console.log(sum);

console.timeEnd("f");
