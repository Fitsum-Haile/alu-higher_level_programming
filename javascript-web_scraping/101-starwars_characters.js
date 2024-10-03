#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
