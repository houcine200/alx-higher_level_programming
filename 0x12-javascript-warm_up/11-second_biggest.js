#!/usr/bin/node

let max = Number.MIN_SAFE_INTEGER;
let second = Number.MIN_SAFE_INTEGER;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    const curr = parseInt(process.argv[i]);
    if (curr > max) {
      second = max;
      max = curr;
    } else if (curr > second && curr < max) {
      second = curr;
    }
  }
  console.log(second);
}
