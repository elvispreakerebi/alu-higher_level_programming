#!/usr/bin/node
const fs = require('fs');

// Get the file path and string from the arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Check if both arguments are provided
if (!filePath || !content) {
  console.error('Error: Missing file path or content');
  process.exit(1); // Exit the script with a failure code
}

// Write the content to the file in utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);  // Print the error object if an error occurs
  }
});
