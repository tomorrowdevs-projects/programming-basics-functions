const prompt = require('prompt-sync')({sigint: true});

console.log("Il seguente programma centra una stringa nella finestra in cui è visualizzata!\n");

const sentence = prompt("Inserisci una frase: => ");
const windowsLength = Number(prompt("Quant'è larga la finestra delle schermo? => "));

if (sentence.length >= windowsLength) console.log("\nATTENZIONE! Inserire una frase più corta della finestra!");

console.log("\nRISULTATO:");

showCenteredString(sentence, windowsLength);


function showCenteredString(s, w = 50) {

    if (s.length >= w) return console.log(s);
    
    const spaceAmount = Math.trunc( (w - s.length) / 2 );

    let space = "";
    for (let i = 0; i < spaceAmount; i++) space += " ";

    if ( (w - s.length) % 2 === 0) {
        return console.log(space + s + space + "|");
    }
    else {
        return console.log(space + s + space + " |");
    }
}