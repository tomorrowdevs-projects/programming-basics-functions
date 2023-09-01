console.log("Dimostrazione della funzione 'getOrdinal()' :");

for (let i = 1; i < 13; i++) {
    console.log(i + " => " + getOrdinal(i) + ";");
}


function getOrdinal(number) {
    if (number < 1 || number > 12) return "";

    const ordinalNumbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"];

    return ordinalNumbers[number - 1];
}