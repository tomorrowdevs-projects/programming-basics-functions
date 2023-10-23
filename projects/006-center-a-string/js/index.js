'use strict';

function centerString(s, w) {
    let lenght_s = s.length;
    const countSpaces = (w - lenght_s) / 2; // Initialize variable to count the empties spaces
    console.log(parseInt(lenght_s));

    if (lenght_s >= w) {
        console.log(s);
    } else {
        console.log(countSpaces);
    }
    let centeredString =
        countSpaces > 0 ? ' '.repeat(Math.floor(countSpaces)) : '';
    console.log(`${centeredString}${s}${centeredString}`);
}

// main programm
let s = prompt('Enter a sentence or what you desire');

let w = 80;

centerString(s, w);
