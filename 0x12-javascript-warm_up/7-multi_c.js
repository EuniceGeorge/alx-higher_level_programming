#!/usr/bin/node
const args = process.argv;
let x = args[2];
if (isNaN(parseInt(x)) === true){
	console.log('Missing number of occurrences');
} else {
	console.log('C is fun' , 2);
}
