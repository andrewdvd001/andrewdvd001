//task 1
function delay() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("Login Finished");
        }, 2000);
    });
}

async function testLogin() {
    console.log("Testing Login...")
    let result = await delay();
    console.log(result);
}
testLogin();

//task 2
function connected() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("Server Connected");
        }, 3000);
    });
}

async function checkServer() {
    let result = await connected();
    console.log(result);
}
checkServer();