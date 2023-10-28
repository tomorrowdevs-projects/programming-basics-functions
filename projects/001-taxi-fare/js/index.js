'use strict';
function taxiFare(distanceTravelledInMeters) {
    // const totalFare =
    //     distanceTravelledInMeters < metersSupplement
    //         ? `The total fare is €${baseFare.toFixed(2)}.`
    //         : `The total fare is €${(supplementFare + baseFare).toFixed(2)}`;
    // return totalFare;
    if (distanceTravelledInMeters < metersSupplement) {
        return `The total fare is €${baseFare.toFixed(2)}.`;
    } else if (
        distanceTravelled === '' ||
        distanceTravelled === ' ' ||
        distanceTravelled === ' , ' ||
        isNaN(distanceTravelled)
    ) {
        return `Insert a valid number`;
    } else {
        return `The total fare is €${(supplementFare + baseFare).toFixed(2)}`;
    }
}

const baseFare = 4;
const supplementPrice = 0.25;
const metersSupplement = 140;

const distanceTravelled = Number(
    prompt(
        'Enter the distance travelled in kilometres. For the addition of any decimal numbers, type a dot (e.g. 1.20)'
    )
);
const distanceTravelledInMeters = distanceTravelled * 1000;

// Fare calculation based on kilometres entered (converted to metres)
const supplementFare =
    (distanceTravelledInMeters / metersSupplement) * supplementPrice;

const fareMessage = taxiFare(distanceTravelledInMeters);
console.log(fareMessage);
