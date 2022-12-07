#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (let x = list.length - 1; x >= 0; x--) {
    rev.push(list[x]);
  }
  return rev;
};
