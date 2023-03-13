#!/usr/bin/node
const num = process.argv[2];

if (isNaN(parseInt(num))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let outPut = '';
    for (let j = 0; j < num; j++) {
      outPut += 'X';
    }
    console.log(outPut);
  }
}
