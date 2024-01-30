#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw error;
  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  }

  console.log(completedTasksByUser);
});
