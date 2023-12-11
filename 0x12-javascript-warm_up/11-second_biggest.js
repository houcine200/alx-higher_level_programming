#!/usr/bin/node

let max = 0;
let second = 0;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > max) {
      second = max;
      max = parseInt(process.argv[i]);
    }
  }
  console.log(second);
}
