'use strict';

const lenghtPassword = Math.floor(Math.random() * (10 - 7 + 1) + 7); // Set 10 as the maximum and 7 as the minimum.
console.log(lenghtPassword);

let randomPassword = ' ';

for (let i = 1; i <= lenghtPassword; i++) {
    const randomNumber = Math.floor(Math.random() * (126 - 33 + 1) + 33);

    randomPassword += randomNumber + ' ';
}
console.log(randomPassword);
let convertedRandomPassword = String.fromCharCode(randomPassword);
console.log(convertedRandomPassword);
