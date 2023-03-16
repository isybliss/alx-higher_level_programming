#!/usr/bin/node
// function that returns the number of searchElement in a list

exports.nbOccurences = function (list, searchElement) {
  return (list.map((value) => (value === searchElement)).length);
};
