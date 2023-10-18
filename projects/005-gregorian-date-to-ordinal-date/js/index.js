'use strict';

const date = Number(prompt('Enter an integer between 1 to 31'));
const month = Number(prompt('Enter an integer between 1 to 12'));
const year = Number(prompt('Enter an year'));

// Check is year is a leap year and check if year is an integer
if (
    (year % 4 === 0 && year % 100 !== 0) ||
    (year % 4 === 0 && year % 100 === 0 && year % 400 === 0)
) {
    console.log(`${year} is a leap year`);
} else if (year === '' || year === ' ' || isNaN(year)) {
    cl('Enter a valid integer');
} else {
    console.log(`${year} is not a leap year`);
}
