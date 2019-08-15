import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))
MM,DD,YY = map(int,input().split())
dict_week = {0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURSDAY",6:"SUNDAY"}
print(dict_week[calendar.weekday(YY,MM,DD)])