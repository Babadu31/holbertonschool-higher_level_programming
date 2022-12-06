#!/usr/bin/node
const count = process.argv.lenght;
console.log(count === 2
  ? 'No argument'
  : count === 3
    ? 'Argument found'
    : 'Argument found');
