'use strict';

function hex2int(hexadecimalDigit) {
    const lengthStringHexDigit = hexadecimalDigit.length;
    let result = 0;

    for (let i = 0; i < lengthStringHexDigit; i++) {
        const currentChar = hexadecimalDigit[i];
        let digit = 0;

        if (currentChar >= '0' && currentChar <= '9') {
            digit = parseInt(currentChar, 16); // Directly convert the numbers from '0' to '9
        } else if (
            (currentChar >= 'A' && currentChar <= 'F') ||
            (currentChar >= 'a' && currentChar <= 'f')
        ) {
            digit = currentChar.charCodeAt(0) - 'A'.charCodeAt(0) + 10; // Converts letters A to F to upper or lower case
        } else {
            console.log('Input typed is not a valid hexadecimal character.');
            break;
        }

        digit = parseInt(currentChar, 16);
        console.log(digit);

        result = result * 16 + digit;
    }
    return result;
}

const hexadecimalDigit = prompt(
    'Enter a hexadecimal number by entering a number from 0 to 9 or letters from A to F (in upper or lower case).'
);

const numdecimal = hex2int(hexadecimalDigit);

console.log(`Decimal equivalent: ${numdecimal}`);

function int2hex(insertNumber) {
    const numberEsadecimale = insertNumber.toString(16).toUpperCase();
    return `Hexadecimal equivalent: ${numberEsadecimale}`;
}
const insertNumber = Number(prompt('Enter a single or multi-digit number'));

const hexNumber = int2hex(insertNumber);
console.log(hexNumber);
