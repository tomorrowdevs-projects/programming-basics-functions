const prompt = require('prompt-sync')({sigint: true});

const passwordLength = Number( prompt("Quanto deve essere lunga la tua password? => ") );

const password = getRandomPassword(passwordLength);

console.log(getHidePassword(password));

const showPassword = prompt("Vuoi vedere la password? => [Si/No] : ").toUpperCase();

if (showPassword === "SI") console.log(password);


function getRandomPassword(length) {

    const excludedRange = [43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64];

    let randomChar;
    do {
        randomChar = Math.floor((Math.random() * 90) + 33);
    } while (excludedRange.includes(randomChar));

    if (length === 1) {
        return String.fromCharCode(randomChar);
    }

    const password = String.fromCharCode(randomChar) + getRandomPassword(length -1);

    return password;
}

function getHidePassword(somePassword) {
    let newPassword = "";

    for (let i = 0; i < somePassword.length; i++) {
        newPassword += "#";
    }

    return newPassword;
}