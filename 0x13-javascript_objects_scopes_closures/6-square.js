#!/usr/bin/node
// class square that defines a square and inherits from class square
// of 5-square.js

const Square_ = require('./5-square');

class Square extends Square_ {
  charPrint (c) {
    if (c) {
      let outPut = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          outPut = outPut + c;
        }
        console.log(outPut);
        outPut = '';
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
