#!/usr/bin/node
const SquareB = require('./5-square');
module.exports = class Square extends SquareB {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let A = '';
      for (let x = 0; x < this.width; x++) {
        A += c;
      }
      for (let x = 0; x < this.height; x++) {
        console.log(A);
      }
    }
  }
};
