'use strict';

function getSecurePassword() {
    return password;
}
const desiredPasswordLength = Number(
    prompt('Enter the number of characters you want your password to contain')
);
// console.log(desiredPasswordLength);
// console.log(typeof desiredPasswordLength);

let password = '';

for (let i = 1; i <= desiredPasswordLength; i++) {
    const randomCharachter = Math.floor(Math.random() * (126 - 33 + 1) + 33);
    password += String.fromCharCode(randomCharachter + '');
}

const generatedPassword = getSecurePassword();
console.log(generatedPassword);
