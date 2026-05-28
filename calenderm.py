import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# str = c.formatmonth(2026, 1, 0, 0) 
# print(str)
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# str1 = hc.formatmonth(2026, 1)
# print(str1)

# for i in c.itermonthdays(2026, 8):
#     print(i)
# for name in calendar.month_name:
#     print(name)
# for day in calendar.day_name:
#     print(day)  
print("Team meeting will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2026, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.TUESDAY] != 0:
        meetday = weekone[calendar.TUESDAY]
    else:
        meetday = weektwo[calendar.TUESDAY]
    print("%10s %2d" % (calendar.month_name[m], meetday))