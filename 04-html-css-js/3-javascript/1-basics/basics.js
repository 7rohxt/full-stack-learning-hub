// Run with: node 01_fundamentals.js

// -----------------------------------
// Variables
// -----------------------------------

let name = "Rohit";
const age = 24;

console.log(name, age);

// -----------------------------------
// Data Types
// -----------------------------------

let isStudent = true;
let skills = ["Python", "FastAPI"];
let user = { name: "Rohit", age: 24 };

console.log(isStudent, skills, user);

// -----------------------------------
// Functions (regular + arrow)
// -----------------------------------

function greet(n) {
    return `Hello ${n}`;
}

const greetArrow = (n) => {
    return `Hello ${n}`;
};

console.log(greet("Rohit"), "|", greetArrow("Rohit"));

// -----------------------------------
// if / else
// -----------------------------------

if (age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}

// -----------------------------------
// Loops
// -----------------------------------

const nums = [1, 2, 3];
for (const num of nums) {
    console.log(num);
}

// -----------------------------------
// Objects
// -----------------------------------

console.log(user.name);

// -----------------------------------
// Arrays
// -----------------------------------

const fruits = ["Apple", "Banana"];
fruits.push("Orange");
console.log(fruits);


// -----------------------------------
// JSON
// -----------------------------------

const json = JSON.stringify(user);
const obj = JSON.parse(json);
console.log(json, "->", obj);