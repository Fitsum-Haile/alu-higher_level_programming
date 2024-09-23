#!/usr/bin/node

const firstArg = process.argv[2];
if (firstArg === undefined || isNaN(parseInt(firstArg))) {
  console.log('Missing number of occurrences');
} else {
  const parsedArg = parseInt(firstArg);
  if (parsedArg < 0) {
    // do nothing
  } else {
    for (let i = 0; i < parsedArg; i++) {
      console.log('C is fun');
    }
  }
}
