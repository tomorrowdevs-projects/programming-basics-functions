'use strict';

function centerString(s, w) {
    if (lenght_s >= w) {
        return s;
    } else {
        return countSpaces;
    }
}

// main programm
let s = prompt('Enter a sentence or what you desire');
let w = 80;
let lenght_s = s.length;

const countSpaces = (w - lenght_s) / 2; // Initialize variable to count the empties spaces
console.log(parseInt(lenght_s));

let centeredString = countSpaces > 0 ? ' '.repeat(Math.floor(countSpaces)) : '';
console.log(`${centeredString}${s}${centeredString}`);

centerString(s, w);
