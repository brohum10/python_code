
investment_amount = float(input("Enter investment amount: "))
annual_interest = float(input("Enter annual interest rate: "))
num_years = float(input("Enter number of years: "))
#1200 is for percentage and divided by 12 for months
future_value = ((investment_amount)*((1+(annual_interest/1200))**(num_years*12)))
print("Accumulated value is ", future_value)
