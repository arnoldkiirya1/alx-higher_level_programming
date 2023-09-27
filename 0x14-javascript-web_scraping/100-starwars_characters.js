#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the command line argument
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Check if a movie ID is provided as an argument
if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Make a GET request to the SWAPI endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    
    // Fetch and display character names
    fetchCharacterNames(characters);
  } else {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});

function fetchCharacterNames(characterUrls) {
  const characterPromises = characterUrls.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request.get(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        } else {
          reject(error || `Failed to fetch character data. Status code: ${response.statusCode}`);
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      console.log(characterNames.join('\n'));
    })
    .catch(error => {
      console.error(error);
      process.exit(1);
    });
}
