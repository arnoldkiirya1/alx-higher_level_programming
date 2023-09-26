#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the command line argument

// Check if a file path is provided as an argument
if (!filePath) {
  console.error('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

// Read the file content in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred during reading
    console.error(err);
    process.exit(1);
  }

  // Print the content of the file
  console.log(data);
});
