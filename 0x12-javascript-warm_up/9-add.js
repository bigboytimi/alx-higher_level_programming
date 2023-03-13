#!/usr/bin/node

const num1 = Math.floor(Number(process.argv[2]));
const num2 = Math.floor(Number(process.argv[3]));

if (isNaN(num1) || isNaN(num2)){
	console.log("Nan");
}else {
	const sum = add(num1, num2);
	console.log(sum);
}

function add(one, two){
	const sum =  one + two;
	return sum;
}
