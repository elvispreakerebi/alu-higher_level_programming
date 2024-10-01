#!/usr/bin/node
const fs = require('fs');

// Get the file path from the first argument
const filePath = process.argv[2];

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);  // Print the error object if an error occurs
  } else {
    console.log(data); // Print the file content if reading succeeds
  }
});
