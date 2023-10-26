'use strict';
function capitalize_it(newString) {
    if (
        (newString.includes('. ') ||
            newString.includes('! ') ||
            newString.includes('? ') ||
            newString.includes(' i ') ||
            newString.includes(' i.')) === true
    ) {
        console.log(
            `${letterToCapitalize
                .concat(stringToSlice)
                .replace(letterI, letterI.toUpperCase())
                .replace(letterUpperCase, letterUpperCase.toUpperCase())}`
        );
    } else {
        return { newString };
    }
}

// main programm

let stringToCapitalize = prompt('Enter a sentence');
const letterToCapitalize = stringToCapitalize.charAt(0).toUpperCase();
const stringToSlice = stringToCapitalize.slice(1);
let newString = console.log(`${letterToCapitalize.concat(stringToSlice)}`);

newString = stringToCapitalize;

const letterI = ' i ';
capitalize_it();
