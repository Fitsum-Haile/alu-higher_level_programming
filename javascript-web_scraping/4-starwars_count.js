#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = '18';
const wedgeAntillesUrl = `https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.includes(wedgeAntillesUrl)) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
