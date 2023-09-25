function addTime(clockHours = isRequired(), duration = isRequired(), weekDay) {
    let meridian = clockHours.slice(-2).toUpperCase();

    const startTime = clockHours.slice(0, -2).split(":");
    duration = duration.split(":");

    let newClockHours = Number(startTime[0]) + Number(duration[0]);
    let newClockMinutes = Number(startTime[1]) + Number(duration[1]);

    if (newClockMinutes > 60) {
        newClockMinutes = newClockMinutes - 60;
        newClockHours ++;
    }

//-------COMPUTING DAYS SECTION-----------------

    let days = Math.trunc(newClockHours / 24);
    let addedDays = "";

    if (newClockHours % 24 > 0 ) {

        if ( ( (newClockHours % 24) + Number(startTime[0]) ) > 12 && meridian === "PM") {
            days++;
        }

    }

    if (days === 1) {
        addedDays = " (next day)";
    }
    else if (days > 1) {
        addedDays = " (" + days + " days later)";
    }

//------COMPUTING OPTIONAL DAY OF THE WEEK-------------

    let newWeekDay = "";

    if (weekDay != undefined) {
        const weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

        weekDay = weekDay[0].toUpperCase() + weekDay.toLowerCase().slice(1);

        newWeekDay = ", " + weekdays[weekdays.indexOf(weekDay) + days];
    }

    if (newClockHours >= 12) {

        if ( Math.trunc(newClockHours / 12) % 2 != 0 ) {
            meridian = (meridian === "AM") ? "PM" : "AM";
        }

        if ( (newClockHours % 12) === 0) {
            newClockHours = Number(startTime[0]) + 1;
        }
        else {
            newClockHours = newClockHours % 12;
        }

    }

    if (newClockHours < 10 || newClockMinutes < 10){
        newClockHours = newClockHours.toString().padStart(2, "0");
        newClockMinutes = newClockMinutes.toString().padStart(2, "0");
    }

    const newTime = newClockHours + ":" + newClockMinutes + " " + meridian + newWeekDay + addedDays;

    return newTime;
}


console.log( addTime("3:00 PM", "3:10") );
console.log( addTime("11:30 AM", "2:32", "Monday") );
console.log( addTime("11:43 AM", "00:20") );
console.log( addTime("10:10 PM", "3:30") );
console.log( addTime("11:43 PM", "24:20", "tueSday") );
console.log( addTime("6:30 PM", "205:12") );