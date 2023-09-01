const prompt = require('prompt-sync')({sigint: true});

let itemsPurchased;

while (true) {
    itemsPurchased = Number( prompt("Quanti prodotti hai nel carrello? => ") );

    if (itemsPurchased === 0) {
        console.log("Non hai acquistato alcun prodotto!");
    }
    else if ( isNaN(itemsPurchased) || Number.isInteger(itemsPurchased) !== true || itemsPurchased < 0 ) {
        console.log("Inserisci un valore corretto!");
    }
    else {
        break;
    }
}

console.log("Totale spese di spedizione: " + calcShippingFees(itemsPurchased) + " euro.");


function calcShippingFees (items) {
    let shippingFees = 10.99;
    const additionalItemShipping = 2.99;

    if (items > 1) ( shippingFees += ( additionalItemShipping * (items - 1) ) );
    return shippingFees.toFixed(2);
}