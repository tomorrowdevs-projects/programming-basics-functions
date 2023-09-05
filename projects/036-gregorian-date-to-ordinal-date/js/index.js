const prompt = require('prompt-sync')({sigint: true});

let day;
let month;
let year;
while (true) {
    day = Number( prompt("Inserire giorno: => ") );
    month = Number( prompt("Inserire mese: => ") );
    year = Number( prompt("Inserire anno: => ") );

        
        if (month <= 12) {
        
            switch (month) {
            case 4:
            case 6:
            case 9:
            case 11:

                if (day < 31) {
                    break;
                }
                else {
                    day = 0;
                }
                

            break;
            
            case 2:
    
                if ( (year % 4 === 0) || (year % 400 === 0) ) {

                    if (day < 30) {
                        break;
                    }
                    else {
                        day = 0;
                    }

                }
                else {

                    if (day < 29) {
                        break;
                    }
                    else {
                        day = 0;
                    }

                }
    
            break;
    
            default:

                if (day < 32) {
                    break;
                }
                else {
                    day = 0;
                }

            }
        
            if (isNaN(day + month + year) != true && day > 0 && month > 0 && year > 0) {

                break;

            }
        }
    

    console.log("ERRORE! Inserire solo numeri interi positivi.");
}

console.log("Il giorno dell'anno è: " + calcOrdinalDate(day, month, year) + "! Sotto forma di data ordinale.");

function calcOrdinalDate(day, month, year) {

    if (month === 1) return day;

    month--;
    switch (month) {
        case 4:
        case 6:
        case 9:
        case 11:
            monthsDays = 30;
        break;
        
        case 2:

            if ( (year % 4 === 0) || (year % 400 === 0) ) 
                monthsDays = 29;
            else 
                monthsDays = 28;

        break;

        default:
            monthsDays = 31;
    }

    return day + calcOrdinalDate(monthsDays, month, year);
}