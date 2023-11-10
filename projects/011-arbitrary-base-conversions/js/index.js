'use strict';

function arbitraryBaseToBase10() {
    if (base >= 2 && base <= 16 && !isNaN(inputNumber)) {
        const resultNumber = parseInt(inputNumber, base); //
        return `The final result is: ${resultNumber} in base 10.`;
    } else {
        return 'Invalid input or base';
    }
}

function base10ToArbitraryBase() {
    if (base >= 2 && base <= 16 && !isNaN(inputNumber)) {
        const resultNumber2 = inputNumber.toString(base).toUpperCase();
        return `The final result is: ${resultNumber2} in base ${base}.`;
    } else {
        return 'Invalid input or base';
    }
}

// programm main
const inputNumber = Number(prompt('Enter a number'));
const base = Number(prompt('Enter a number between 2 and 16'));

const resultBase10 = arbitraryBaseToBase10();
console.log(resultBase10);

const resultBaseArbitrary = base10ToArbitraryBase();
console.log(resultBaseArbitrary);
