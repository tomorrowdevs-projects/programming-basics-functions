'use strict';

function daysInAMonth(month, year) {
    if (month === 1 && year >= 1000 && year <= 9999) {
        // Year between 1000 and 9999, as it must be 4 characters long
        return `In January ${year} there are 31 days.`;
    } else if (
        month === 2 &&
        year >= 1000 &&
        year <= 9999 &&
        year % 4 !== 0 &&
        year % 100 !== 0 &&
        year % 400 !== 0
    )
        return `In February ${year} there are 28 days, because the chosen year is not a leap year.`;
    else if (
        month === 2 &&
        year >= 1000 &&
        year <= 9999 &&
        year % 4 === 0 &&
        year % 100 === 0 &&
        year % 400 === 0
    ) {
        return `In February ${year} there are 29 days, because the chosen year is a leap year.`;
    } else if (month === 3 && year >= 1000 && year <= 9999) {
        return `In March ${year} there are 31 days.`;
    } else if (month === 4 && year >= 1000 && year <= 9999) {
        return `In April ${year} there are 30 days.`;
    } else if (month === 5 && year >= 1000 && year <= 9999) {
        return `In May ${year} there are 31 days.`;
    } else if (month === 6 && year >= 1000 && year <= 9999) {
        return `In June ${year} there are 30 days.`;
    } else if (month === 7 && year >= 1000 && year <= 9999) {
        return `In July ${year} there are 31 days.`;
    } else if (month === 8 && year >= 1000 && year <= 9999) {
        return `In August ${year} there are 31 days.`;
    } else if (month === 9 && year >= 1000 && year <= 9999) {
        return `In September ${year} there are 30 days.`;
    } else if (month === 10 && year >= 1000 && year <= 9999) {
        return `In October ${year} there are 31 days.`;
    } else if (month === 11 && year >= 1000 && year <= 9999) {
        return `In November ${year} there are 30 days.`;
    } else if (month === 12 && year >= 1000 && year <= 9999) {
        return `In December ${year} there are 31 days.`;
    } else {
        return 'Incorrect input';
    }
}

// Main programm
const month = Number(prompt('Enter a number between 1 and 12'));
const year = Number(prompt('Enter a 4-digit number'));

const result = daysInAMonth(month, year);
console.log(result);
