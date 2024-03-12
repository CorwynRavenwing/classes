import calendar

(MM, DD, YYYY) = tuple(map(int, input().split()))
# print("#MM DD YYYY", MM, DD, YYYY)
weekday = calendar.weekday(YYYY, MM, DD)
# print("#W", weekday)
day_name = calendar.day_name[weekday]
print(day_name.upper())

