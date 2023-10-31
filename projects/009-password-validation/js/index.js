'use strict';

function passwordValidation() {
    if (isUpperCase && isLowerCase && hasNumber) {
        return 'The password is valid';
    } else {
        return 'Insert a new password';
    }
}

const password = prompt('Enter a password');
const lenghtPassword = password.length;

let isUpperCase = false;
let isLowerCase = false;
let hasNumber = false;

for (let i = 0; i < lenghtPassword; i++) {
    const checkPassword = password.charCodeAt(i);

    if (checkPassword >= 65 && checkPassword <= 90) {
        isUpperCase = true;
    } else if (checkPassword >= 97 && checkPassword <= 122) {
        isLowerCase = true;
    } else if (checkPassword >= 48 && checkPassword <= 57) {
        hasNumber = true;
    } else {
        console.log('Insert something');
    }
}

const result = passwordValidation();
console.log(result);
