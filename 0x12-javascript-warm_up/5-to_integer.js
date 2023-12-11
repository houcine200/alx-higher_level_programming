#!/usr/bin/node
num = parseInt(process.argv[2]);
console.log(num);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
