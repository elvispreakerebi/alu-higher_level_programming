#!/usr/bin/node
const request = require('request');

// Get the API URL from the command-line arguments
const url = process.argv[2];

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);  // Print any error that occurs during the request
  } else {
    // Parse the response body (which is in JSON format)
    const todos = JSON.parse(body);
    const completedTasks = {};

    // Loop through the todos and count completed tasks for each user
    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId] += 1;
      }
    });

    // Print the result
    console.log(completedTasks);
  }
});
