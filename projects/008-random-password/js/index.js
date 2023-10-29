'use strict';

function randomPassword() {
    return Password;
}

// main Programm
const lenghtPassword = Math.floor(Math.random() * (10 - 7 + 1) + 7); // Set 10 as the maximum and 7 as the minimum.
console.log(lenghtPassword);
console.log(typeof lenghtPassword);

let Password = '';

for (let i = 1; i <= lenghtPassword; i++) {
    const randomNumber = Math.floor(Math.random() * (126 - 33 + 1) + 33);
    Password += String.fromCharCode(randomNumber) + ' ';
}

const result = randomPassword();
console.log(result);
