const { input } = require("./input.js");
console.time("f");
const data = input.split("\n");

const mapLineLengthToIndex = {
  2: 1,
  6: 2,
  10: 3,
  14: 4,
  18: 5,
  22: 6,
  26: 7,
  30: 8,
  34: 9
};

const initializeStacks = () => {
  const stacks = {};
  [1, 2, 3, 4, 5, 6, 7, 8, 9].forEach(x => (stacks[x] = []));

  for (line of data) {
    if (line === "") {
      break;
    }
    let lineLength = 0;
    for (char of line) {
      lineLength += 1;
      if (char.match(/[a-z]/i)) {
        stacks[mapLineLengthToIndex[lineLength]].unshift(char);
      }
    }
  }
  return stacks;
};

const move = (stacks, numMoves, from, to, reverse = false) => {
  const cache = [];
  for (let i = 0; i < numMoves; i++) {
    const crate = stacks[from].pop();
    if (reverse) {
      cache.unshift(crate);
    } else {
      stacks[to].push(crate);
    }
  }
  if (reverse) {
    stacks[to] = [...stacks[to], ...cache];
  }
};

const getInstructionsAndMove = (stacks, reverse = false) => {
  for (line of data) {
    if (line.match(/^(move)/)) {
      let instructions = line.match(/\d+/gm);
      if (reverse === true) {
        move(stacks, instructions[0], instructions[1], instructions[2], true);
      } else {
        move(stacks, instructions[0], instructions[1], instructions[2]);
      }
    }
  }
};

const getTopCratesString = stacks => {
  return Object.values(stacks)
    .map(x => x[x.length - 1])
    .join("");
};

const part1 = () => {
  const stacks = initializeStacks();
  getInstructionsAndMove(stacks);
  return getTopCratesString(stacks);
};

const part2 = () => {
  const stacks = initializeStacks();
  getInstructionsAndMove(stacks, true);
  return getTopCratesString(stacks);
};

console.log("Part 1: ", part1());
console.log("Part 2: ", part2());

console.timeEnd("f");
