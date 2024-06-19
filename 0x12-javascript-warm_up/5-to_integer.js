#!/usr/bin/node
const args = process.argv;
const val = parseInt(args[2]);
if (isNaN(val) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + val);
}
