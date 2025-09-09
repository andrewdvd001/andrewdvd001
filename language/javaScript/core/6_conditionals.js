
let bugs = 150
let tools = "Cypress"
let active = true;

if (bugs > 100) {
    console.log(`Block Release`);
} else if (bugs > 50) {
    console.log(`Needs QA review`);
} else {
    console.log(`Release OK`);
}

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

