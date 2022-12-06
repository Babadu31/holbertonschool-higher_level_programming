#!/usr/bin/node
let x = 0;
process.argv.forEach(() => {
  x++;
});
if (x === 3) {
  console.log('Argument found');
} else if (x <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
