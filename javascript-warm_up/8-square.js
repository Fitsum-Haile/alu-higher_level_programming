#!/usr/bin/node

const firstArg = process.argv[2];
const parsedArg = parseInt(firstArg);
if (parsedArg === undefined || isNaN(parsedArg)) {
  console.log('Missing size');
} else if (parsedArg < 0) {
// do nothing
} else {
  for (let i = 0; i < parsedArg; i++) {
    let row = '';
    for (let j = 0; j < parsedArg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
