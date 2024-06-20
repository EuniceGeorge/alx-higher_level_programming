#!/usr/bin/node
const args = process.argv;
const len = parseInt(args[2]);
let i;
let j;

if ((isNaN(len)) === true) {
  console.log('Missing size');
} else {
  for (i = 0; i < len; i++) {
    let row = '';
    for (j = 0; j < len; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
