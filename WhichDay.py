# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

dt = input()
dtList = dt.split()
print(calendar.day_name[calendar.weekday(int(dtList[2]), int(dtList[0]), int(dtList[1]))].upper())
