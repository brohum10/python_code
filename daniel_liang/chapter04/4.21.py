year = eval(input("Enter year: (eg., 2008): "))

m = eval(input("Enter month: 1-12: "))

if m == 1 or m == 2:
    m += 12
    year -= 1

q = eval(input("Enter the day of the month: 1-31: "))


j = int(year / 100)
k = (year % 100) 


h = ((q + (26*(m + 1)/10) + k + int(k/4) + int(j/4) + (5*j) )% 7)//1


if h == 0:
    print("Day of the week is Saturday")
if h == 1:
    print("Day of the week is Sunday")
if h == 2:
    print("Day of the week is Monday")
if h == 3:
    print("Day of the week is Tuesday")
if h == 4:
    print("Day of the week is Wednesday")
if h == 5:
    print("Day of the week is Thursday")
if h == 6:
    print("Day of the week is Friday")
