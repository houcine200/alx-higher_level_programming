#!/usr/bin/node

const size = parseInt(process.argv[2]);
let row = '';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      row += ('X');
    }
    if (i !== size - 1) {
      row += ('\n');
    }
  }
  console.log(row);
}
