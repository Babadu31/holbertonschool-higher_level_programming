#!/usr/bin/node
const limite = parseInt(process.argv[2]);
if (limite) {
  for (let x = 0; x < limite; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
