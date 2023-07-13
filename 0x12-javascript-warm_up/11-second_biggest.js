#!/usr/bin/node
function second (myArg) {
  if (myArg.length === 2 || myArg.length === 3) {
    return (0);
  }

  let max = myArg[2];
  let secondMax = myArg[3];

  for (let i = 3; i < myArg.length; i++) {
    if (myArg[i] > max) {
      secondMax = max;
      max = myArg[i];
    } else if (myArg[i] > secondMax && myArg[i] < max) {
      secondMax = myArg[i];
    }
  }
  return (secondMax);
}

console.log(second(process.argv));
