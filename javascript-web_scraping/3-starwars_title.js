#!/usr/bin/node

const request = require('request');
const MovieId = process.arv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + MovieId;

request
  .get(url, function (error, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).tittle);
    }
  });
