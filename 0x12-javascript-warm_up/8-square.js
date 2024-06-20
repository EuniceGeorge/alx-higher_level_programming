#!/usr/bin/node
const args = process.argv;
len = parseInt(args[2]);
let i, j, row;

if ((isNaN(len)) === true) {
  console.log('Missing size');
} else {
  for (i = 0; i < len; i++) {
	  row = '';
	  for (j = 0; j < len; j++) {
		  row += 'x';
	  }
	  console.log(row);
  }
}
