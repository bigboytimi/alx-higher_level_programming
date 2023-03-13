#!/usr/bin/node

const count = process.argv[2];
const num = Math.floor(Number(count));
console.log(isNaN(num) ? "Not a number" : "My number: " + num);
