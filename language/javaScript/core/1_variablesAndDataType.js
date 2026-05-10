let city = "Yogyakarta";
const birthYear = 1995;
let age = 29;
age = 30;

let isQA = true;
let nickname = "Andrew";
let nothing = null;
let future;

console.log(`Born in ${city} at ${birthYear} and now is ${age} years old`);
console.log(`Type of variable of:`);
console.log(`isQA is ` + typeof isQA);
console.log(`nickname is ` + typeof nickname);
console.log(`nothing is ` + typeof nothing);
console.log(`future is ` + typeof future);

const x = 15;
const y = 4;

let sum = x + y;
let difference = x - y;
let product = x * y;
let division = x / y;
let modulus = x % y;

console.log(`Sum of x and y is ${sum}, difference is ${difference}, product is ${product}, division is ${division}, and modulus is ${modulus}`);
console.log(x > y);
console.log(x < y);
console.log(x == y);
console.log(x === y);
console.log(10 == "10");
console.log(10 === "10");
switch (tools) {
    case "Selenium":
        console.log("Selenium running ...");
        break;
    case "Cypress":
        console.log("Cypress running ...");
        break;
    case "Playwright":
        console.log("Playwright running ...")
        break;
    default:
        console.log("Unknown tool selected.")
    
}

let status = active ? "Tester is active" : "Tester is not active";
console.log(status);

