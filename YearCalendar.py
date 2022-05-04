import calendar as cal

year= int(input("What year do you want a calendar for?"))
for i in range(1, 13):
    print(cal.month(year, i))