const startDate = new Date(90, 0, 1);
const endDate = new Date(99, 11, 31);

const twentyCenturyDates = getDateRange(startDate, endDate);

for (const date of twentyCenturyDates) {

    if (checkMagicDates(date) === true) {
        console.log("Data magica: => " + date.toLocaleDateString());
    }
}


function checkMagicDates(date) {

    const day = date.getDate();
    const month = date.getMonth() + 1;
    const year = date.getFullYear();

    const last2DigitYear = Number( year.toString().substring(2) );

    if ( (day * month) === last2DigitYear) {
        return true;
    }

    return false;
}

function getDateRange(startDate, endDate) {
    
    const dateRange = [];

    for (let i = 0, nextDate = startDate; nextDate.getTime() <= endDate.getTime(); i++) {
        dateRange[i] = nextDate;
        nextDate = new Date(nextDate.getTime() + 86400000);
    }

    return dateRange;
}