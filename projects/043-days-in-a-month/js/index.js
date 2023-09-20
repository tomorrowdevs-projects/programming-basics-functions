function getMonthTotalDays(month, year) {
    const months31 = [1, 3, 5, 7, 8, 10, 12];

    if ( months31.includes(month) ) return 31;

    else if (month === 2) {

        if (year % 4 === 0 || year % 400 === 0) return 29;
        else return 28;

    }

    else return 30;
}


const prompt = require('prompt-sync')({sigint: true});

let month;
let year;

while (true) {

    const monthsAsNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

    month = Number( prompt("Mese: => ") );
    year = parseInt( prompt("Anno: => ") );

    if ( (month + year) !== NaN && year.toString().length === 4 && monthsAsNumber.includes(month)) {
        break;
    }

    console.log("Input errato! Inserie solo numeri interi.");
}

console.log( getMonthTotalDays(month, year) );