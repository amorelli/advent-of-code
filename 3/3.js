const { input } = require("./input.js");
console.time("f");
const data = input.split("\n");

const charValues = (() => {
  const values = {};
  const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  for (let i = 0; i < chars.length; i++) {
    values[chars[i]] = i + 1;
  }
  return values;
})();

const uniqueLetters = string => {
  const unique = {};
  for (letter of string) {
    if (unique[letter]) {
      continue;
    } else {
      unique[letter] = 1;
    }
  }
  return unique;
};

const getSumOfSharedChars = () => {
  let sum = 0;
  for (i = 0; i < data.length; i++) {
    const half = Math.floor(data[i].length / 2);
    const firstHalf = data[i].slice(0, half);
    const secondHalf = data[i].slice(half);
    for (char of secondHalf) {
      if (uniqueLetters(firstHalf)[char]) {
        sum = sum + charValues[char];
        break;
      }
    }
  }
  return sum;
};

const sharedLetters = (one, two) => {
  const shared = {};
  const firstLetters = Object.keys(one);
  const secondLetters = Object.keys(two);
  for (i = 0; i < firstLetters.length; i++) {
    if (secondLetters.includes(firstLetters[i])) {
      shared[firstLetters[i]] = 1;
    }
  }
  return shared;
};

const getSumOfBadges = () => {
  let sum = 0;
  for (let i = 0; i < data.length - 2; i += 3) {
    const unique1 = uniqueLetters(data[i]);
    const unique2 = uniqueLetters(data[i + 1]);
    const unique3 = uniqueLetters(data[i + 2]);
    const badge = sharedLetters(sharedLetters(unique1, unique2), unique3);
    const value = charValues[Object.keys(badge)[0]];
    sum = sum + value;
  }
  return sum;
};

console.log("Problem 1: ", getSumOfSharedChars());
console.log("Problem 2: ", getSumOfBadges());
console.timeEnd("f");
