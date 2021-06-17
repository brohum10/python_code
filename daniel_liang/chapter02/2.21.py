savings = eval(input("Enter the monthly saving amount: "))

formula = (1 + 0.00417)

month_1 = savings*formula
month_2 = (savings+month_1)*formula
month_3 = (savings+month_2)*formula
month_4 = (savings+month_3)*formula
month_5 = (savings+month_4)*formula
month_6 = (savings+month_5)*formula

print("After the sixth month, the account value is %.2f" %month_6)
