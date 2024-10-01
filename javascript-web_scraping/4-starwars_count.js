#!/usr/bin/node
const request = require('request');

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Wedge Antilles has character ID 18
const wedgeAntillesId = '18';

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);  // Print any error that occurs
  } else {
    const films = JSON.parse(body).results;  // Parse the response body and get the list of films
    let count = 0;

    // Loop through each film
    films.forEach((film) => {
      // Check if Wedge Antilles (character ID 18) is in the film's characters list
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    });

    console.log(count);  // Print the number of films Wedge Antilles is in
  }
});
