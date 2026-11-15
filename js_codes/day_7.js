// projects

// calculator
// steps are:
// create a function that takes two numbers and an operation

// function calculator(a, b, op){
//     a = Number(a), b = Number(b);
//     if(op === "+") return a+b;
//     else if(op === "-") return a-b;
//     else if(op === "*") return a*b;
//     else if(op === "/") return b === 0? "cannot divide by 0": a/b;
//     else return "unknown operator"
// }

// answer = calculator(23, 45, "/")
// result = calculator(23, 0, "/")

// console.log(result)

// GUESSING GAME (browser prompt version)
const secret = Math.floor(Math.random() * 20) + 1;
let tries = 0;
let guess = 0;
while (guess !== secret) {
  guess = Number(prompt("Guess 1-20"));
  tries++;
  if (guess < secret) console.log("Too low!");
  else if (guess > secret) console.log("Too high!");
}
console.log("You won in " + tries + " tries!");