#!/usr/bin/node

const fs = require('fs');

// Retrieve the file paths from the command line arguments
const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

// Read the contents of the first file
fs.readFile(file1Path, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1Path}:`, err);
    process.exit(1);
  }

  // Read the contents of the second file
  fs.readFile(file2Path, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2Path}:`, err);
      process.exit(1);
    }

    // Concatenate the contents and write to the destination file
    const concatenatedData = data1 + data2;
    fs.writeFile(destinationPath, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationPath}:`, err);
        process.exit(1);
      }
      console.log(`Files successfully concatenated to ${destinationPath}`);
    });
  });
});
