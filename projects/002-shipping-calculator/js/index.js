'use strict';
function shippingCalculator(totalItem) {
    if (totalItem > 1) {
        return alert(
            `The total number of purchase is ${totalItem}. Total shipping is €${totalShipping.toFixed(
                2
            )}.`
        );
    } else if (
        totalItem <= 0 ||
        totalItem === '' ||
        totalItem === ' ' ||
        isNaN(totalItem)
    ) {
        alert('Enter a number greater than 0');
    } else {
        return alert(
            `The total number of purchase is ${totalItem}. Total shipping is €${firstItem}.`
        );
    }
}

function main() {
    let firstItem = 10.99;
    let subsequentItem = 2.99;
    let totalItem = Number(
        prompt('How many items would you like to ship overall?')
    );

    // Variable initialised for total shipping cost
    const totalShipping = alert(
        ((totalItem - 1) * subsequentItem + firstItem).toFixed(2)
    );
}

main();
