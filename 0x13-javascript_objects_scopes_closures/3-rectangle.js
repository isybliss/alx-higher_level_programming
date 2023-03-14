#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
      let outPut = ''
      for (let i = 0; i < h; i++) {
        for (let j = 0; j < w; j++) {
          outPut = outPut + 'X';
	}
	console.log(outPut);
      }
  }

module.exports = Rectangle;
