'use strict';

function getSecurePassword(length) {
    let password = '';

    for (let i = 1; i <= length; i++) {
        const randomCharachter = Math.floor(
            Math.random() * (220 - 33 + 1) + 33
        );
        password += String.fromCharCode(randomCharachter);
    }
    return password;
}

function hidePassword(password) {
    return 'x'.repeat(password.length);
}
const desiredPasswordLength = Number(
    prompt('Enter the number of characters you want your password to contain')
);

const getSecurePasswordGenerated = getSecurePassword(desiredPasswordLength);
const hiddenPassword = hidePassword(getSecurePasswordGenerated);

console.log(hiddenPassword);
console.log(getSecurePasswordGenerated);
