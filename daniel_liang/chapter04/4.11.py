month, year = eval(input("Enter the month and it's year in numbers: "))

#Check for leap year
leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

if month == 1:
    month = 'January'
    monthdays = 31
elif month == 2:
    month = 'February'
    if leap_year == 0:
        monthdays = 28
    else:
        monthdays = 29
elif month == 3:
    monthdays = 31
    month = 'March'
elif month == 4:
    monthdays = 30
    month = 'April'
elif month == 5:
    monthdays = 31
    month = 'May'
elif month == 6:
    monthdays = 30
    month = 'June'
elif month == 7:
    monthdays = 31
    month = 'July'
elif month == 8:
    monthdays = 31
    month = 'August'
elif month == 9:
    monthdays = 31
    month = 'September'
elif month == 10:
    monthdays = 31
    month = 'October'
elif month == 11:
    monthdays = 30
    month = 'November'
elif month == 12:
    monthdays = 31
    month = 'December'

print(month, year, "has ", monthdays, "days")
    

