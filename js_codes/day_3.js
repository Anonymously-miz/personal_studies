// const name = "Ava";
// const ageText = "17"; // from an input box - always a string!

// const age = Number(ageText);
// console.log(typeof ageText); // "string"
// console.log(typeof age);      // "number"
// console.log("Next year you will be " + (age + 1));

// // Template literal - cleaner joining
// console.log(`Hi ${name}, you are ${age} years old.`);

// // Common gotcha
// console.log("5" + 5); // "55" - string wins
// console.log(Number("5") + 5); // 10

// used variables from day_2.js
const myName = "Ishmail Abass Kamara";
const career = ["Backend Engineer", "Remote Backend Engineer"];
const winningMindset = true;
let age = 25;
let myClass = "semester 8";
const account = {
    "id": 1,
    "Account name": "Ishmail",
    "Balance": 34000000
}
let city = "Freetown";

// console.log(typeof(myName));
// console.log(typeof(career));
// console.log(typeof(winningMindset));
// console.log(typeof(age));
// console.log(typeof(myClass));
// console.log(typeof(account));

let textNumber = '99';
console.log(Number(textNumber) + 1);

console.log(`My name is ${myName} and I live in ${city}`);

// null is a type for variables that holds no value intentionally and undefined is a type for a variable that has not been given any value.