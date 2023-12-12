#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let raw = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        raw += c;
      }
      if (i !== this.height - 1) {
        raw += '\n';
      }
    }
    console.log(raw);
  }
}
module.exports = Square;
