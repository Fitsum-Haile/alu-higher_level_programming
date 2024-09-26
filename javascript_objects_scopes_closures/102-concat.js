#!/usr/bin/node

const fs = require('fs');
const path = require('path');

const [fileA, fileB, fileC] = process.argv.slice(2);

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(`Error reading ${fileA}:`, err);
    return;
  }

  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(`Error reading ${fileB}:`, err);
      return;
    }

    fs.writeFile(fileC, dataA + dataB, (err) => {
      if (err) {
        console.error(`Error writing to ${fileC}:`, err);
        return;
      }
      console.log(`Successfully concatenated ${fileA} and ${fileB} into ${fileC}`);
    });
  });
});
