// Functions work either if the user wants to convert numbers greater than 2^53 or not.

console.log( getHextoDec("145798DCB") ); //Argument is only for example

console.log( getDectoHex(773738363261118345n) ); //Argument is only for example


function getHextoDec(s) {
    s = s.toUpperCase();

    const hexLetters = ["A", "B", "C", "D", "E", "F"];

    const base = 16;
    let Dec = 0;
    let decDigit = 0;

    for (let i = 0; i < s.length; i++) {
        let hexChar = s.at(- (1 + i) );

        if ( hexLetters.includes(hexChar) ) {
            hexChar = hexChar.codePointAt(0) - 55;
        }
        decDigit = Number(hexChar) * Math.pow(base, i);

        if (Dec > Math.pow(2, 53)) {
            Dec = BigInt(Dec);
            decDigit = BigInt(decDigit);
            console.log("Ciao");
        }

        Dec = decDigit + Dec;
    }

    return Dec;
}


function getDectoHex(n) {
    let base = 16;

    if (typeof n === "bigint") {
        base = 16n;
    }

    const hexLetters = { 
        10 : "A", 
        11 : "B", 
        12 : "C", 
        13 : "D", 
        14 : "E", 
        15 : "F"
    };

    if (n < base) {        
        if (n in hexLetters) {
            return hexLetters[n];
        }
        return n;
    }

    const nextDecDigit = getDectoHex( Math.trunc( Number(n / base) ) );
    let nextHexDigit = n % base;

    if (nextHexDigit in hexLetters) {
        nextHexDigit = hexLetters[nextHexDigit];
    }

    return nextDecDigit + nextHexDigit.toString();
}

// getDectoHex(): While-loop-version

/* function DectoHex(number) {

    const hexLetters = { 
        10 : "A", 
        11 : "B", 
        12 : "C", 
        13 : "D", 
        14 : "E", 
        15 : "F"
    };

    let hex = "";
    while (number > 0) {
        let hexDigit = number % base;
       
        if (hexDigit in hexLetters) {
            hexDigit = hexLetters[hexDigit];
        }
    
        hex = hexDigit + hex;
        number = Math.trunc(number / base);
    } 

    return hex;
} */