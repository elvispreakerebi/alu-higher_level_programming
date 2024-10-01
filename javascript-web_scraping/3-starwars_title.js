#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Define the API URL with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);  // Print any error that occurs
  } else {
    const data = JSON.parse(body);  // Parse the response body as JSON
    console.log(data.title);        // Print the title of the movie
  }
});
