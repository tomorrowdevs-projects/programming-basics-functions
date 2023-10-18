'use strict';
function verseSong(verse) {
    switch (verse) {
        case 1:
            alert(
                `On the first day of Christmas my true love sent to me: ${firstVerse}.`
            );
            break;
        case 2:
            alert(
                `On the second day of Christmas my true love sent to me: ${secondVerse}.`
            );
            break;
        case 3:
            alert(
                `On the third day of Christmas my true love sent to me: ${thirdVerse}.`
            );
            break;
        case 4:
            alert(
                `On the fourth day of Christmas my true love sent to me: ${fourthVerse}.`
            );
            break;
        case 5:
            alert(
                `On the fifth day of Christmas my true love sent to me: ${fifthVerse}.`
            );
            break;
        case 6:
            alert(
                `On the sixth day of Christmas my true love sent to me: ${sixthVerse}.`
            );
            break;
        case 7:
            alert(
                `On the seventh day of Christmas my true love sent to me: ${seventhVerse}.`
            );
            break;
        case 8:
            alert(
                `On the eighth day of Christmas my true love sent to me: ${eighthVerse}.`
            );
            break;
        case 9:
            alert(
                `            On the ninth day of Christmas my true love sent to me: ${ninthVerse}.`
            );
            break;
        case 10:
            alert(
                `On the tenth day of Christmas my true love sent to me: ${tenthVerse}.`
            );
            break;
        case 11:
            alert(
                `On the eleventh day of Christmas my true love sent to me: ${eleventhVerse}.`
            );
            break;
        case 12:
            alert(
                `On the twelth day of Christmas my true love sent to me: ${twelthVerse}.`
            );
            break;
        default:
            alert(' ');
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
const twelthVerse = `twelve drummers drumming, ${eleventhVerse.toLowerCase()}`;

verseSong(verse);

for (let i = 1; i <= 12; i++) {
    verseSong(i);
}
