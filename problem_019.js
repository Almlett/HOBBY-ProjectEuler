/* Problem 19 project euler */
const months = {
    'January':31,
    'February':28,
    'March':31,
    'April':30,
    'May':31,
    'June':30,
    'July':31,
    'August':31,
    'September':30,
    'October':31,
    'November':30,
    'December':31
}

const days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

const leapYear = year => {
    if (year % 100 === 0 && year % 400 === 0){
        return true;
    }
    if (year % 4 === 0){
        return true;
    }
    return false;
}

const yearDays = () => {
    let sum = 0;
    for (const month in months) {
        sum += months[month]
    }
    return sum;
}

const getMonth = day => {
    
    let sum = 0;
    for (const month in months) {
        sum += months[month]
        if (day < sum) {
            return month
        }
    }
    return 1;
}


const startYear = 1901;

let currentDay = 0;
let count = 0;
/*
Lunes = 0
Domingo = 6
*/

for (let year = 1900; year <= 2000; year++) {
    if (leapYear(year)){
        months.February = 29
    }else{
        months.February = 28
    }

    let month = '';
    let previousMonth = '1';
    //console.log("______ ", year, " ______")
    for (let day = 0; day < yearDays(); day++) {
        month = getMonth(day);
        if (month !== previousMonth){
            //console.log(`Month:${month} - previousMonth:${previousMonth}`)
            previousMonth = month;
            if (currentDay === 6 && year >= startYear){
                count ++;
            }
        }else{
            //console.log(`Month:${month} - previousMonth:${previousMonth}`)
        }

        currentDay = currentDay === 6 ? 0 : currentDay + 1;

    }
}
console.log(count)
