#!/usr/bin/node
const util = require('util');
const request = require('request');

const id = process.argv[2];
const reqPromis = util.promisify(request);

request.get(`https://swapi-api.alx-tools.com/api/films/${id}/`, async function (err, resp) {
  if (err) {
    console.error(err);
  } else {
    const people = JSON.parse(resp.body).characters;
    for (const i in people) {
      try {
        const response = await reqPromis(people[i]);
        console.log(JSON.parse(response.body).name);
      } catch (err) {
        console.error(err);
      }
    }
  }
});
