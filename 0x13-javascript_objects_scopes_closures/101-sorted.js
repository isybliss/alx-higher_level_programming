#!/usr/bin/node
// import dictionary of occurence by user Id
// compute dictionary of user ids by occurrences

const { dict } = require('./101-data');
const nDict = {};
for (const N in dict) {
  if (nDict[dict[N]] === undefined) {
    nDict[dict[N]] = [];
  }
  nDict[dict[N]].push(N);
}
console.log(nDict);
