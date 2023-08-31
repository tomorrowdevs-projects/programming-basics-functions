const prompt = require('prompt-sync')({sigint: true});

let kilometersDone;
do {
kilometersDone = Number(prompt("Quanti km hai percorso durante la tua ultima corsa in Taxi? => "));
} while ( isNaN(kilometersDone) || kilometersDone < 0 );

console.log("Totale da pagare: " + taxiFare(kilometersDone) + " euro.");

function taxiFare(km) {
    const additionalFare= ((km * 100) / 14) * 0.25;
    const baseFare = 4;
    const totalFare = baseFare + Number(additionalFare.toFixed(2));
    return totalFare;
}