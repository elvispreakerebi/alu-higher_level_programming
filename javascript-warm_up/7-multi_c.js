#!/usr/bin/node

const str = 'C is fun';
const args = process.argv.slice(2);
let num = args[0];

if (args.length === 0) {
  console.log('Missing number of occurrences');
} else {
  while (num !== 0) {
   console.log(str);
   num--;
  }
}
