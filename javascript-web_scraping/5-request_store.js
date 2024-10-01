#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);  // Print any error that occurs during the request
  } else {
    // Write the body (response content) to the specified file
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);  // Print any error that occurs while writing the file
      }
    });
  }
});
