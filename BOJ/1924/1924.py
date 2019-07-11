import calendar
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
a, b = map(int, input().split())
k = calendar.weekday(2007, a, b)
print(day[k])