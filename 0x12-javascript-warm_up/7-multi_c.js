#!/usr/bin/node

const isNum = parseInt(process.argv[2]);

if (isNaN(isNum)) {
  console.log('Missing number of occurrences')
} else {
  for (let i = 0; i < isNum; i++) {
    console.log('C is fun');
  }
}
