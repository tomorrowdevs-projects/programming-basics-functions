'use strict';

const integer = Number(prompt('Enter a number from 1 to 12'));

function integerToOrdinal(integer) {
    switch (integer) {
        case 1:
            alert(
                `The number entered is ${integer} and its English ordinal is First.`
            );
            break;
        case 2:
            alert(
                `The number entered is ${integer} and its English ordinal is Second.`
            );
            break;
        case 3:
            alert(
                `The number entered is ${integer} and its English ordinal is Third.`
            );
            break;
        case 4:
            alert(
                `The number entered is ${integer} and its English ordinal is Fourth.`
            );
            break;
        case 5:
            alert(
                `The number entered is ${integer} and its English ordinal is Fifth.`
            );
            break;
        case 6:
            alert(
                `The number entered is ${integer} and its English ordinal is Sixth.`
            );
            break;
        case 7:
            alert(
                `The number entered is ${integer} and its English ordinal is Seventh.`
            );
            break;
        case 8:
            alert(
                `The number entered is ${integer} and its English ordinal is Eighth.`
            );
            break;
        case 9:
            alert(
                `The number entered is ${integer} and its English ordinal is Ninth.`
            );
            break;
        case 10:
            alert(
                `The number entered is ${integer} and its English ordinal is Tenth.`
            );
            break;
        case 11:
            alert(
                `The number entered is ${integer} and its English ordinal is Eleventh.`
            );
            break;
        case 12:
            alert(
                `The number entered is ${integer} and its English ordinal is Twelth.`
            );
            break;
        default:
            alert(' ');
    }
}
integerToOrdinal(integer);
