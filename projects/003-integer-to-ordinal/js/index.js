'use strict';

function integerToOrdinal(integer) {
    switch (integer) {
        case 1:
            return `First.`;
            break;
        case 2:
            return `Second.`;
            break;
        case 3:
            return `Third.`;
            break;
        case 4:
            return `Fourth.`;
            break;
        case 5:
            return `Fifth.`;
            break;
        case 6:
            return `Sixth.`;
            break;
        case 7:
            return `Seventh.`;
            break;
        case 8:
            return `Eighth.`;
            break;
        case 9:
            return `Ninth.`;
            break;
        case 10:
            return `Tenth.`;
            break;
        case 11:
            return `Eleventh.`;
            break;
        case 12:
            return `Twelth.`;
            break;
        default:
            return ' ';
    }
}

// Main programm
const integer = Number(prompt('Enter a number from 1 to 12'));
const ordinal = integerToOrdinal(integer);
if (ordinal) {
    console.log(
        `The number entered is ${integer} and its English ordinal is ${ordinal}`
    );
} else {
    console.log('Invalid input!');
}
for (let i = 1; i <= 12; i++) {
    integerToOrdinal(i);
}
