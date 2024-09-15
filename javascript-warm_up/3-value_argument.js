#!/usr/bin/node

const args = process.argv.slice(2);

if (args.indexOf(args[0]) === -1) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
