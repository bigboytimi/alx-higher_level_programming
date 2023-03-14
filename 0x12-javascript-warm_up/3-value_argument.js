#!/usr/bin/node

const count = process.argv;
console.log(typeof count[2] === 'undefined' ? 'No argument' : count[2]);
