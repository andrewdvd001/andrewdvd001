let users = [
    { name: "Andrew", age: 25 },
    { name: "Budi", age: 16 },
    { name: "Citra", age: 30 }
];

function ageValidator(age) {
    if (age >= 18) {
        return `Adult`
    } else {
        return `Underage`
    };
}

for (let counter = 0; counter < (users.length); counter++ ){
        let name = users[counter].name
        let age = users[counter].age
        console.log(name + ` - ` + ageValidator(age))
}
