'use strict';
function reduceMeasures(unitNumber, measureUnit) {
    const cupEquivalence = Math.trunc(unitNumber / 16);
    const remainingTablespoons = unitNumber % 16;
    const cupTablespoonEquivalence = Math.trunc(unitNumber / 48);
    const teespoonEquivalence = unitNumber % 48; // In case there is no tablespoon
    const tableTeespoonEquivalence = Math.trunc(teespoonEquivalence / 3);
    const remainingTeespoon = remainingTablespoons % 3;

    let result;
    if (
        measureUnit === 'cup' &&
        (measureUnit !== ' ' || measureUnit !== '' || isNaN(measureUnit)) &&
        unitNumber > 0 &&
        !isNaN(unitNumber)
    ) {
        result = console.log(
            `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${unitNumber} ${measureUnit.toLowerCase()}s.`
        );
    } else if (
        measureUnit === 'tablespoon' &&
        (measureUnit !== ' ' || measureUnit !== '' || isNaN(measureUnit)) &&
        unitNumber > 0 &&
        !isNaN(unitNumber)
    ) {
        if (cupEquivalence >= 1 && remainingTablespoons === 0) {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${cupEquivalence} cups.`
            );
        } else if (unitNumber < 16) {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${unitNumber} ${measureUnit.toLowerCase()}s.`
            );
        } else if (cupEquivalence >= 1 && remainingTablespoons !== 0) {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${cupEquivalence} cups and ${remainingTablespoons} tablespoons.`
            );
        } else {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${remainingTablespoons} tablespoons.`
            );
        }
    } else if (
        measureUnit === 'teaspoon' &&
        (measureUnit !== ' ' || measureUnit !== '' || isNaN(measureUnit)) &&
        unitNumber > 0 &&
        !isNaN(unitNumber)
    ) {
        if (unitNumber <= 2) {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${unitNumber} ${measureUnit.toLowerCase()}s.`
            );
        } else if (unitNumber >= 48 && remainingTablespoons === 0) {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${cupTablespoonEquivalence} cups.`
            );
        } else if (unitNumber >= 48 && remainingTablespoons <= 2) {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${cupTablespoonEquivalence} cups and ${remainingTablespoons} teaspoons.`
            );
        } else if (
            unitNumber >= 48 &&
            teespoonEquivalence >= 3 &&
            tableTeespoonEquivalence === 0
        ) {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${cupTablespoonEquivalence} cups and ${tableTeespoonEquivalence} tablespoons.`
            );
        } else if (
            unitNumber >= 48 &&
            teespoonEquivalence >= 3 &&
            tableTeespoonEquivalence !== 0
        ) {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${cupTablespoonEquivalence} cups, ${tableTeespoonEquivalence} tablespoons and ${remainingTeespoon} teespoons.`
            );
        } else {
            result = console.log(
                `Depending on the entered parameters (${unitNumber} ${measureUnit}s), you will need these for your recipe: ${tableTeespoonEquivalence} tablespoons and ${remainingTeespoon} teespoons.`
            );
        }
    } else {
        console.log(
            'Incorrect input. Please enter a valid number or choose one of the given units.'
        );
    }
}

// main programm
const measureUnit = prompt(
    'Select the unit of measurement you need to prepare your recipe. Choose from the following options Cup, Tablespoon or Teaspoon'
).toLowerCase();

const unitNumber = Number(prompt('Enter the number of units required'));

reduceMeasures(unitNumber, measureUnit);
