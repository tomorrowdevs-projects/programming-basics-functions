'use strict';
function shippingCalculator(totalItem) {
    if (totalItem > 1) {
        const totalShipping = (
            (totalItem - 1) * subsequentItem +
            firstItem
        ).toFixed(2);
        return `The total number of purchase is ${totalItem}. Total shipping is €${totalShipping}.`;
    } else if (
        totalItem <= 0 ||
        totalItem === '' ||
        totalItem === ' ' ||
        isNaN(totalItem)
    ) {
        return 'Enter a number greater than 0';
    } else {
        return `The total number of purchase is ${totalItem}. Total shipping is €${firstItem}.`;
    }
}

let firstItem = 10.99;
let subsequentItem = 2.99;
let totalItem = Number(
    prompt('How many items would you like to ship overall?')
);

const calculatorMessage = shippingCalculator(totalItem);
console.log(calculatorMessage);
