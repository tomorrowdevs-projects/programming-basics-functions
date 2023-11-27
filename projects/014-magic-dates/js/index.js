'use strict';

function checkMagicDates(month, day, yearLastTwoDigits) {
    function getMonth(month) {
        // to get the corresponding month in letters for the month in numbers from the user
        switch (month) {
            case 1:
                return 'January';
                break;
            case 2:
                return 'February';
                break;
            case 3:
                return 'March';
                break;
            case 4:
                return 'April';
                break;
            case 5:
                return 'May';
                break;
            case 6:
                return 'June';
                break;
            case 7:
                return 'July';
                break;
            case 8:
                return 'August';
                break;
            case 9:
                return 'September';
                break;
            case 10:
                return 'October';
                break;
            case 11:
                return 'November';
                break;
            case 12:
                return 'December';
                break;
            default:
                return 'The entered input is not valid';
        }
    }

    const monthInLetters = getMonth(month);

    // I have stored some conditions in some variables that I do not want to repeat later.
    const leapYear = Number(
        (yearLastTwoDigits % 4 === 0 && yearLastTwoDigits % 100 !== 0) ||
            (yearLastTwoDigits % 4 === 0 &&
                yearLastTwoDigits % 100 === 0 &&
                yearLastTwoDigits % 400 === 0)
    );

    const monthsWith31Days =
        (day <= 31 && month <= 7 && month % 2 === 1) ||
        month === 8 ||
        month === 10 ||
        month === 12
            ? true
            : false;

    const monthsWith30Days =
        day <= 30 && (month === 4 || month === 6 || month === 9 || month === 11)
            ? true
            : false;

    const februaryNotLeapYear =
        day <= 28 && month === 2 && year !== leapYear ? true : false;

    const februaryIsLeapYear =
        day <= 29 && month === 2 && year === leapYear ? true : false;
    // First if the date entered is correct
    if (
        month * day === yearLastTwoDigits &&
        month >= 1 &&
        month < 12 &&
        day >= 1 &&
        day <= 31 &&
        year >= 1900 &&
        year <= 1999 &&
        (monthsWith31Days === true ||
            monthsWith30Days === true ||
            februaryNotLeapYear === true ||
            februaryIsLeapYear === true)
    ) {
        return `${monthInLetters} ${day}, ${year} is a magic date`;
    } else if (
        month * day !== yearLastTwoDigits &&
        month >= 1 &&
        month < 12 &&
        day >= 1 &&
        day <= 31 &&
        year >= 1900 &&
        year <= 1999 &&
        (monthsWith31Days === true ||
            monthsWith30Days === true ||
            februaryNotLeapYear === true ||
            februaryIsLeapYear === true)
    ) {
        return `${monthInLetters} ${day}, ${year} is not a magic date`;
    } else {
        return 'The entered date is not valid';
    }
}

// main programm
const month = Number(prompt('Enter a month between 1 and 12'));
const day = Number(prompt('Enter a day between 1 and 31'));
const year = prompt('Enter a year between 1900 and 1999'); // I do not enter the Number() method, because I need to extrapolate the last two numbers from the string

const yearLastTwoDigits = Number(year.slice(2));

// Nested for loops to see the magical dates of the 20th century
for (let yearLastTwoDigits = 0; yearLastTwoDigits <= 99; yearLastTwoDigits++) {
    for (let month = 1; month <= 12; month++) {
        for (let day = 1; day <= 31; day++) {
            const allMagicDates =
                month * day === yearLastTwoDigits &&
                yearLastTwoDigits >= 10 &&
                yearLastTwoDigits <= 99
                    ? console.log(
                          `${day} - ${month} - 19${yearLastTwoDigits} is a magic date`
                      )
                    : month * day === yearLastTwoDigits &&
                      yearLastTwoDigits >= 1 &&
                      yearLastTwoDigits <= 9
                    ? console.log(
                          `${day} - ${month} - 190${yearLastTwoDigits} is a magic date`
                      )
                    : '';
            console.log(allMagicDates);
        }
    }
}

const resultMagicDates = checkMagicDates(month, day, yearLastTwoDigits);
console.log(resultMagicDates);
