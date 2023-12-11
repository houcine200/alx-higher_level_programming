#!/usr/bin/node

const n = parseInt(process.argv[2]);

function Factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  } else {
    return n * Factorial(n - 1);
  }
}
const result = Factorial(n);
console.log(result);
