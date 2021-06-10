

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5/9
    print(temp, " in fahrenheit is equal to ", celsius, "in celsius.")

def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    print(temp, " in celsius is equal to ", fahrenheit, "in fahrenheit.")

type = input("Enter 'F' for fahrenheit and 'C' for celsius:\n")    
temp = float(input("Enter temperature in Fahrenheit or Celsius:\n"))

if type == "F":
    fahrenheit_to_celsius(temp)
if type == "C":
    celsius_to_fahrenheit(temp)
