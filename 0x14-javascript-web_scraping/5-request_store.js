#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) throw error;
  fs.writeFile(fileName, body, 'utf8', function (err) {
    if (err) console.log(err);
  });
});
