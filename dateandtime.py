from datetime import date
from datetime import datetime
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
t = datetime.now()
print(t)
d = date.today()
print(d)
w = d.weekday()
print(w)
print(days[w])
t1 = datetime.time(datetime.now())
print(t1)