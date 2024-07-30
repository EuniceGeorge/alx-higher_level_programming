#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];
const content = process.argv[3];
fs.writeFileSync(filepath, content, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }
  console.log(data);
});
