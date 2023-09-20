function getOneBase2Another(string, startBase, endBase) {
    
    const toBaseTen = parseInt(string, startBase);

    return toBaseTen.toString(endBase).toUpperCase();
}


function getDec2Base(number, newbase) {

    const baseRange = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];

    if (baseRange.includes(newbase) != true) {
        const error = "Choose a base between 2 and 16!";
        return error;
    }

    return number.toString(newbase).toUpperCase();
}


function getToBase10(string, base) {

    const baseRange = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];

    if (baseRange.includes(base) != true) {
        const error = "Choose a base between 2 and 16!";
        return error;
    }

    return parseInt(string, base);
}

const prompt = require('prompt-sync')({sigint: true});

const number = prompt("Numero: => ");
const actualBase = Number( prompt("Base: => ") );
const newBase = Number( prompt("Nuova base: => ") );

let result = "";
if (actualBase === 10) {
    result = getDec2Base(Number(number), newBase);
}
else if (newBase === 10){
    result = getToBase10(number, actualBase);
}
else {
    result = getOneBase2Another(number, actualBase, newBase);
}

console.log("Risultato in base " + newBase + ": => " + result);