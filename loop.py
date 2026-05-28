days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    if day == "Wednesday":
        continue
    if day == "Friday":
        break
    print(day)
    
for i,d in enumerate(days):
     print(i, d)
