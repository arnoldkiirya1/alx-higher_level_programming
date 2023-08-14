#!/usr/bin/node

function secondBiggest(numbers) {
  numbers.sort((a, b) => b - a);
  if (numbers.length <= 1) {
    return 0;
  } else {
    return numbers[1];
  }
}

const args = process.argv.slice(2).map(Number);

console.log(secondBiggest(args));
