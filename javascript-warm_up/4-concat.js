#!/usr/bin/node
/*  a script that prints two arguments passed to
  it, putting 'is' in beteween the two arguments. */

const firstArg = process.argv[2];
const secondArg = process.argv[3];

console.log(firstArg + ' is ' + secondArg);
