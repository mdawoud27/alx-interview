#!/usr/bin/node

const axios = require('axios');
const movieID = process.argv[2];

const getCharacters = async (movieId) => {
  try {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    const response = await axios.get(url);
    const characters = response.data.characters;

    for (const character of characters) {
      const characterResponse = await axios.get(character);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
};

getCharacters(movieID);
