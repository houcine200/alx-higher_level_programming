#!/usr/bin/node

exports.esrever = function (list) {
  for (let i = 0; i < list.length / 2; i++) {
    const swap = list[i];
    list[i] = list[list.length - 1 - i];
    list[list.length - 1 - i] = swap;
  }
  return list;
};
