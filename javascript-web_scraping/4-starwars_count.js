#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  let count = 0;
  if (error) throw (error);
  const data = JSON.parse(body);
  for (let x = 0; data.results[x] !== undefined; x++) {
    if (data.results[x].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
