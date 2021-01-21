function getDates() {
    let today = new Date();
    let month = today.getMonth() + 1;
    let day = today.getDate();
    
    let dates = [];
    let dateToChinese = {
        "0": "天",
        "1": "一",
        "2": "二",
        "3": "三",
        "4": "四",
        "5": "五",
        "6": "六"
    };

    if (day - 7 <= 0) {
        let lastMonth, lastMonthDay
        
        if (month - 1 == 0) {
            lastMonth = 12;
            lastMonthDay = 31;
        } else {
            lastMonth = month - 1;
            lastMonthDay = new Date(today.getFullYear(), lastMonth, 0).getDate();
        }

        for (let thisMonthDayCount = 1 ; thisMonthDayCount <= 7 ; thisMonthDayCount++) {
            if (day - thisMonthDayCount <= 0) {
                for (let lastMonthDayCount = 0 ; lastMonthDayCount <= 7 - thisMonthDayCount ; lastMonthDayCount++) {
                    dates = [
                        `${lastMonth} / ${lastMonthDay - lastMonthDayCount}（${dateToChinese[new Date(today.getFullYear(), lastMonth - 1, lastMonthDay - lastMonthDayCount - 1).getDay()]}）`
                    ].concat(dates);
                }

                break;
            } else {
                dates = [
                    `${month} / ${day - thisMonthDayCount}（${dateToChinese[new Date(today.getFullYear(), month - 1, day - thisMonthDayCount).getDay()]}）`
                ].concat(dates);
            }
        }

        dates = dates.concat([
            `${month} / ${day}（${dateToChinese[new Date(today.getFullYear(), month - 1, day).getDay()]}）`
        ]);

        for (let DayCount = 1 ; DayCount <= 14 ; DayCount++) {
            dates = dates.concat([
                `${month} / ${day + DayCount}（${dateToChinese[new Date(today.getFullYear(), month - 1, day + DayCount).getDay()]}）`
            ]);
        }
    } else if (day + 14 > new Date(today.getFullYear(), month - 1, 0).getDate()) {
        let thisMonthDay = new Date(today.getFullYear(), month - 1, 0).getDate();
        for (let DayCount = 1 ; DayCount <= 7 ; DayCount++) {
            dates = [
                `${month} / ${day - DayCount}（${dateToChinese[new Date(today.getFullYear(), month - 1, day - DayCount).getDay()]}）`
            ].concat(dates);
        }

        dates.push(
            `${month} / ${day}（${dateToChinese[new Date(today.getFullYear(), month - 1, day).getDay()]}）`
        );

        let nextMonth;
        thisMonthDay = new Date(today.getFullYear(), month - 1, 0).getDate();
        
        if (month + 1 == 13) {
            nextMonth = 1;
        } else {
            nextMonth = month + 1;
        }

        for (let thisMonthDayCount = 1 ; thisMonthDayCount <= 14 ; thisMonthDayCount++) {
            if (day + thisMonthDayCount > thisMonthDay) {
                for (let nextMonthDayCount = 1 ; nextMonthDayCount <= 14 - thisMonthDayCount ; nextMonthDayCount++) {
                    dates.push(
                        `${nextMonth} / ${nextMonthDayCount}（${dateToChinese[new Date(today.getFullYear(), nextMonth - 1, nextMonthDayCount).getDay()]}）`
                    );
                }

                break;
            } else {
                dates.push(
                    `${month} / ${day + thisMonthDayCount}（${dateToChinese[new Date(today.getFullYear(), month - 1, day + thisMonthDayCount).getDay()]}）`
                );
            }
        }
    } else {
        for (let DayCount = 1 ; DayCount <= 7 ; DayCount++) {
            dates = [
                `${month} / ${day - DayCount}（${dateToChinese[new Date(today.getFullYear(), month - 1, day - DayCount).getDay()]}）`
            ].concat(dates);
        }

        dates.push(
            `${month} / ${day}（${dateToChinese[new Date(today.getFullYear(), month - 1, day).getDay()]}）`
        );
        
        for (let DayCount = 1 ; DayCount <= 14 ; DayCount++) {
            dates = dates.concat([
                `${month} / ${day + DayCount}（${dateToChinese[new Date(today.getFullYear(), month - 1, day + DayCount).getDay()]}）`
            ]);
        }
    }

    return dates
}