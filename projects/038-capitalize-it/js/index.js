const prompt = require('prompt-sync')({sigint: true});

const userString = prompt("Inserisci una frase da correggere: => ");

console.log("Frase corretta: => " + getCorrectCapitalizedString(userString));


function getCorrectCapitalizedString(string) {

    string = upperCaseI(capitalizeFirsLetter(string));

    for (let i = 0; i < string.length; i++) {     
        
        if ( ["!", "?", "."].includes(string[i]) ) {
            string = string.slice(0, i) + capitalizeFirsLetter(string.slice(i));   
        }
        else {
            continue;
        }
    }

    return string;
}


function capitalizeFirsLetter(string) {
    string = string.split("");

    for (let i = 0; i < string.length; i++) {
        const stringCharcter = string[i].codePointAt(string[i]);

        if ( (stringCharcter > 64 && stringCharcter < 90) || (stringCharcter > 96 && stringCharcter < 123) ) {
            string[i] = string[i].toUpperCase();
            break;
        }
        else {
            continue;
        }
    }

    return string.join("");
}


function upperCaseI(string) {

    for (let i = 0; i < string.length; i++) {

        if (string[i] === "i") {

            if (string[i - 1] === " ") {
             
                if ( ["!", "?", ".", "'", " "].includes(string[i + 1]) ) {
                    string = string.slice(0, i) + capitalizeFirsLetter(string.slice(i));   
                }
            }
        }
    }

    return string;
}