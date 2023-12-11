#!/usr/bin/node
const isNum = parseInt(process.argv[2]);

if (isNaN(isNum)) {
  console.log('Not a number');
} else {
  console.log('My number:', isNum);
}
