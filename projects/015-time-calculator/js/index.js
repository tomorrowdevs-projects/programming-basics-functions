'use strict';
function addTime(startTime, durationTime) {
    const startTime2 = startTime.slice(0, -3).replace(':', '');

    const minutesStartTime = Number(startTime2.slice(-2));
    const hoursStartTime = Number(startTime2.slice(0, -2));

    const minutesDurationTime = Number(durationTime.slice(-2));
    const hoursDurationTime = Number(durationTime.slice(0, -3));
    const totalHours = hoursStartTime + hoursDurationTime;
    const totalMinutes =
        totalHours * 60 + (minutesStartTime + minutesDurationTime);

    const clockFormat = startTime.slice(-2);
    const hoursFromMinutes = totalMinutes / 60;
    const remainingMinutes = totalMinutes % 60;
    const minutesInADay = 1440;
    const minutesUntilThirdDay = minutesInADay * 2 - 1;
    const numberDaysLater = totalMinutes / minutesInADay;
    const totalMinutesWithoutDayLater = totalMinutes % minutesInADay;
    const hoursDaysLater = totalMinutesWithoutDayLater / 60;
    const remainingMinutesDayLater = totalMinutesWithoutDayLater % 60;
    const totalMinutesPM = totalMinutes + 720;
    const hoursFromMinutesPM = totalMinutesPM / 60 - 12;
    const remainingMinutesPM = totalMinutesPM % 60;
    const totalMinutesWithoutDayLaterPM = totalMinutesPM % minutesInADay;
    const hoursDaysLaterPM = totalMinutesWithoutDayLaterPM / 60;
    const remainingMinutesDayLaterPM = totalMinutesWithoutDayLaterPM % 60;

    const clockPM = hoursFromMinutes - 12;
    const checkClockFormat =
        totalMinutes % minutesInADay >= 0 && totalMinutes % minutesInADay <= 719
            ? 'AM'
            : 'PM';

    if (
        totalMinutes >= 0 &&
        totalMinutes < minutesUntilThirdDay &&
        clockFormat === 'AM'
    ) {
        return `${
            totalMinutes < 720
                ? Math.trunc(hoursFromMinutes.toFixed(0))
                : Math.trunc((hoursFromMinutes - 12).toFixed(0))
        }:${remainingMinutes} ${checkClockFormat}`;
    } else if (totalMinutesPM < minutesInADay && clockFormat === 'PM') {
        return `${Math.trunc(
            hoursFromMinutesPM.toFixed(0)
        )}:${remainingMinutesPM} ${clockFormat}`;
    } else if (
        clockFormat === 'AM' &&
        totalMinutes <= minutesUntilThirdDay &&
        totalMinutesWithoutDayLater >= 0 &&
        totalMinutesWithoutDayLater <= 719
    ) {
        return `${
            totalMinutesWithoutDayLater < 720
                ? (hoursDaysLater - 1).toFixed(0)
                : (hoursDaysLaterPM - 12).toFixed(0)
        }:${
            totalMinutesWithoutDayLater < 720
                ? remainingMinutesDayLater
                : remainingMinutesDayLaterPM
        } ${checkClockFormat} (next day)`;
    } else if (
        clockFormat === 'PM' &&
        totalMinutesWithoutDayLaterPM <= minutesUntilThirdDay &&
        totalMinutesWithoutDayLaterPM >= 720
    ) {
        return `${(hoursDaysLaterPM - 12).toFixed(
            0
        )}:${remainingMinutesDayLaterPM} ${clockFormat} (next day)`;
    } else if (clockFormat === 'AM' && totalMinutes >= minutesUntilThirdDay) {
        return `${hoursDaysLater.toFixed(0)}:${
            remainingMinutesDayLater - 12
        } ${checkClockFormat} (${numberDaysLater.toFixed(0)} days later)`;
    } else if (clockFormat === 'PM' && totalMinutesPM >= minutesUntilThirdDay) {
        return `${hoursDaysLaterPM.toFixed(0) - 12}:${
            remainingMinutesDayLaterPM - 12
        } ${checkClockFormat} (${numberDaysLater.toFixed(0)} days later)`;
    } else {
        return 'Input not valid';
    }
}

const startTime = prompt(
    'Enter a start time in 12-hour clock format (ending in AM or PM)'
).toUpperCase();

const durationTime = prompt(
    'Enter a duration time that indicates the number of hours and minutes (in this format XX:XX)'
);

const result = addTime(startTime, durationTime);
console.log(result);
