#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
