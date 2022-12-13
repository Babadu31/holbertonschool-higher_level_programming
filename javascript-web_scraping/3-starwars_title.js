#!/usr/bin/node

const request = require('request');
const MovieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + MovieId;

request(url, function (error, request, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
