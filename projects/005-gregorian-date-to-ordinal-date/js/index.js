'use strict';

function gregorian_to_ordinal_date(day, month, year) {
    if (
        (day <= 31 &&
            year === leapYear &&
            ((month <= 7 && month % 2 === 1) ||
                month === 8 ||
                month === 10 ||
                month === 12)) ||
        (day <= 30 &&
            year === leapYear &&
            (month === 4 || month === 6 || month === 9 || month === 11)) ||
        (day <= 29 && month === 2 && year === leapYear)
    ) {
        return `The date entered corresponds to day no. ${ordinal_date_leap_years}.`;
        // Second condition if it is not a leap year
    } else if (
        (day <= 31 &&
            year !== leapYear &&
            ((month <= 7 && month % 2 === 1) ||
                month === 8 ||
                month === 10 ||
                month === 12)) ||
        (day <= 30 &&
            year !== leapYear &&
            (month === 4 || month === 6 || month === 9 || month === 11)) ||
        (day <= 28 && month === 2 && year !== leapYear)
    ) {
        return `The date entered corresponds to day no. ${ordinal_date_regular_years}.`;
    } else {
        return 'Enter a valid number';
    }
}

// main programm
const day = Number(prompt('Enter an integer between 1 to 31'));
const month = Number(prompt('Enter an integer between 1 to 12'));
const year = Number(prompt('Enter an year'));

const ordinal_date_regular_years =
    30 * (month - 1) + Math.trunc(0.6 * (month + 1)) - 3 + day; // I used the algorithm of the so-called Zeller's congruence method.

const ordinal_date_leap_years =
    30 * (month - 1) + Math.trunc(0.6 * (month + 1)) - 2 + day;

const leapYear =
    (year % 4 === 0 && year % 100 !== 0) ||
    (year % 4 === 0 && year % 100 === 0 && year % 400 === 0);

const result = gregorian_to_ordinal_date(day, month, year);
console.log(result);
