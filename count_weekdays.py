import calendar


def count_weekday_instances(year, month, weekday_name):
    weeklist = calendar.monthcalendar(year, month)
    count = 0
    for week in weeklist:
        print(week[weekday_name])
        if week[weekday_name] != 0:
            count += 1
    return count


count = count_weekday_instances(2026, 5, 3)
print(count)