'use strict';
function verseSong(verse) {
    switch (verse) {
        case 1:
            return `On the first day of Christmas my true love sent to me: ${firstVerse}.`;
            break;
        case 2:
            return `On the second day of Christmas my true love sent to me: ${secondVerse}.`;
            break;
        case 3:
            return `On the third day of Christmas my true love sent to me: ${thirdVerse}.`;
            break;
        case 4:
            return `On the fourth day of Christmas my true love sent to me: ${fourthVerse}.`;
            break;
        case 5:
            return `On the fifth day of Christmas my true love sent to me: ${fifthVerse}.`;
            break;
        case 6:
            return `On the sixth day of Christmas my true love sent to me: ${sixthVerse}.`;
            break;
        case 7:
            return `On the seventh day of Christmas my true love sent to me: ${seventhVerse}.`;
            break;
        case 8:
            return `On the eighth day of Christmas my true love sent to me: ${eighthVerse}.`;
            break;
        case 9:
            return `            On the ninth day of Christmas my true love sent to me: ${ninthVerse}.`;
            break;
        case 10:
            return `On the tenth day of Christmas my true love sent to me: ${tenthVerse}.`;
            break;
        case 11:
            return `On the eleventh day of Christmas my true love sent to me: ${eleventhVerse}.`;
            break;
        case 12:
            return `On the twelfth day of Christmas my true love sent to me: ${twelfthVerse}.`;
            break;
        default:
            return ' ';
    }
}

// programm main
const verse = Number(prompt('Enter an integer between 1 to 12'));

const firstVerse = 'a partridge in a pear tree';
const secondVerse = 'two turtle doves, And a partridge in a pear tree';
const thirdVerse = `three French hens, ${secondVerse}`;
const fourthVerse = `four calling birds, ${thirdVerse.toLowerCase()}`;
const fifthVerse = `five gold rings, ${fourthVerse.toLowerCase()}`;
const sixthVerse = `six geese a-laying, ${fifthVerse.toLowerCase()}`;
const seventhVerse = `seven swans a-swimming, ${sixthVerse.toLowerCase()}`;
const eighthVerse = `eight maids a-milking, ${seventhVerse.toLowerCase()}`;
const ninthVerse = `nine ladies dancing, ${eighthVerse.toLowerCase()}`;
const tenthVerse = `ten lords a-leaping, ${ninthVerse.toLowerCase()}`;
const eleventhVerse = `eleven pipers piping, ${tenthVerse.toLowerCase()}`;
const twelfthVerse = `twelve drummers drumming, ${eleventhVerse.toLowerCase()}`;

if (verse >= 1 && verse <= 12) {
    const result = verseSong(verse);
    alert(result);
} else {
    alert('Insert a valid number');
}

for (let i = 1; i <= 12; i++) {
    verseSong(i);
}

for (let i = 1; i <= 12; i++) {
    const result = verseSong(i);
    console.log(result);
}
