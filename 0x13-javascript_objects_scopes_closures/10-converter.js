#!/usr/bin/node
/* Exports an object with a property named 'converter' */
exports.converter = function (base) {
  /* Returns a function that takes 'num' as a parameter */
  return function (num) {
    /* Converts 'num' to a string representation in the specified base */
    return num.toString(base);
  };
};
