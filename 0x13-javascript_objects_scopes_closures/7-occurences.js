#!/usr/bin/node
// function that returns the number of searchElement in a list

exports.nbOccurences = function (list, searchElement) {
  const len = list.Length;
  let count = 0;
  for (let i = 0; i < len; i++ ) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return (count);
}
