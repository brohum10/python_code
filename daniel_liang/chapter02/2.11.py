final = eval(input("Enter the final account value: "))
annual_interest = eval(input("Enter the annual interest rate in percent: "))
years = eval(input("Enter the number of years: "))

monthly_interest = (annual_interest / 100) / 12
months = 12 * years
initial = final/((1 + monthly_interest)**months)

print("Initial deposit value is", initial)
