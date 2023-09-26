#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the command line argument
const contentToWrite = process.argv[3]; // Get the content to write from the command line argument

// Check if both file path and content are provided as arguments
if (!filePath || !contentToWrite) {
  console.error('Usage: ./1-writeme.js <file_path> <content_to_write>');
  process.exit(1);
}

// Write the content to the file in utf-8 encoding
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurred during writing
    console.error(err);
    process.exit(1);
  }

  console.log('The file has been written successfully.');
});
