#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw error;

  const charList = [];
  const films = JSON.parse(body).results;

  for (const film of films) {
    for (const person of film.characters) {
      if (person.includes('/18/')) {
        charList.push(person);
      }
    }
  }
  console.log(charList.length);
});
