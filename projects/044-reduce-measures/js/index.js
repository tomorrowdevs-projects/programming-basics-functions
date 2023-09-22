function calcRecipeMeasures(number, unit) {

    const measuresUnit = ["cup", "tablespoon", "teaspoon"];

    unit = unit.toLowerCase();

    if (measuresUnit.includes(unit) != true) return "Unit: wrong parameter";

    //let measures;

    const conversionFactorTablespoon = 16;
    const conversionFactorTeaspoon = 4;

    if (unit === measuresUnit[0]) {
        number = Math.trunc(number / 1);

        const measures = number + " " + unit;

        return measures;
    }
    else if (unit === measuresUnit[1]) {

        if ( number < conversionFactorTablespoon) {
            const measures = number + " " + unit;

            return measures;
        }
        else{
            const biggestNumberUnit = Math.trunc(number / conversionFactorTablespoon);
            number = number %  conversionFactorTablespoon;

            const measures = calcRecipeMeasures(biggestNumberUnit, measuresUnit[0]) + ", " + number + " " + measuresUnit[1];

            return measures;
        }
    }
    else {

        if ( number < conversionFactorTeaspoon) {
            const measures = number + " " + unit;

            return measures;
        }
        else{
            const biggestNumberUnit = Math.trunc(number / conversionFactorTeaspoon);
            number = number %  conversionFactorTeaspoon;

            const measures = calcRecipeMeasures(biggestNumberUnit, measuresUnit[1]) + ", " + number + " " + measuresUnit[2];

            return measures;
        }
    }
}

console.log( calcRecipeMeasures(40, "tablespoon"));