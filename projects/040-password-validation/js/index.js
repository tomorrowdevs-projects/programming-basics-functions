const prompt = require('prompt-sync')({sigint: true});

while (true) {
    const password = prompt("Inserisci password: => ");

    if ( getPasswordValidation(password) ) {
        console.log("Password valida!"); 
        break;
    }
    
    console.log("ERRORE! Inserire almeno 8 caratteri comprendenti almeno un numero, una lettera Maiuscola e una lettera minuscola!");   
}

function getPasswordValidation(password) {
    if (password.length < 8) return false;

    if (
        password.search(/[A-Z]/) != -1 && 
        password.search(/[a-z]/) != -1 &&
        password.search(/[0-9]/) != -1
    ) {
        return true;
    }
    else {
        return false;
    }
}