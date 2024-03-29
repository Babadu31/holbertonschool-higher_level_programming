#!/usr/bin/node
const request = require('request');
const myUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(myUrl, async function (error, response, body) {
  if (error) { console.error('error:', error); }
  const filmDict = JSON.parse(body);
  for (const charUrl of filmDict.characters) {
    await new Promise((resolve, reject) => {
      request(charUrl, function (err, response, body) {
        if (error) { reject(err); }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
