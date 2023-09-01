let songVerses = "";
for (let i = 1; i <= 12; i++) {
    console.log("On the " + getOrdinal(i) + " day of Christmas my true love sent to me:");
    songVerses = getVerse(i) + "\n" + songVerses;

    if (i === 1) {
        console.log("A partridge in a Pear Tree.\n")
        continue;
    }

    console.log(songVerses);
}


function getVerse(number) {
    const verses = ["and a partridge in a Pear Tree.", 
                    "2 Turtle Doves,", 
                    "3 French Hens,", 
                    "4 Calling Birds,", 
                    "5 Golden Rings,", 
                    "6 Geese a Laying,", 
                    "7 Swans a Swimming,", 
                    "8 Maids a Milking,", 
                    "9 Ladies Dancing,", 
                    "10 Lords a Leaping,", 
                    "11 Pipers Piping,", 
                    "12 Drummers Drumming"];

    return verses[number - 1]; 
}

function getOrdinal(number) {
    if (number < 1 || number > 12) return "";

    const ordinalNumbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"];

    return ordinalNumbers[number - 1];
}