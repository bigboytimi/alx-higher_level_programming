#!/usr/bin/node

const count = Math.floor(Number(process.argv[2]));
if (typeof count === "undefined"){
	console.log("Missing number of occurences");
} else {
for (let i = 0; i < count; i++){
	console.log("C is fun");
}
}
