let users = [
    { name: "Andrew", age: 25 },
    { name: "Budi", age: 16 },
    { name: "Citra", age: 30 }
];

function ageValidator(age) {
    if (age >= 18) {
        console.log(`Adult`)}
    else {console.log(`Underage`)}
}

function repeater(name){
    for (let counter = 1; counter <= (name.length - 1); counter++ )
        let name = name[counter].name
        let age = age[counter].age
}

function delay() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(users.name + `-` + users.a);
        }, 2000);
    });
}