from datetime import date, datetime
now = datetime.now()
print("Current date and time: ", now)
print(now.strftime("current year is %Y"))
# %B - month name, %d - day of the month, %Y - year with century, %a - abbreviated weekday name
print(now.strftime("%B, %d, %Y, %a"))
today = date.today()
afd = date(today.year,4,1)
if afd < today:
    print(f"April Fools' Day already passed this year by {(today - afd).days} days.") 
    afd = date(today.year + 1,4,1)

time_to_afd = afd - today
print(f"Time to April Fools' Day: {time_to_afd.days} days.")