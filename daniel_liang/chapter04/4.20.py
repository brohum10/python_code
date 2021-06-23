t_a = eval(input("Enter the temperature in Fahrenheit between -58 and 41 : "))
v = eval(input("Enter the wind speed in miles per hour : "))

if v >= 2 and (t_a > -58 and t_a < 41):
    
    t_wc = 35.74 + (0.6215 * t_a) - (35.75 * (v ** 0.16)) + (0.4275 * t_a * (v ** 0.16))
    print("The wind chill is", t_wc)

elif v < 2 and (t_a < -58 or t_a > 41):

    print("Sorry but the wind speed is too small to be evaluated and your temperature is out of range")

elif v < 2:
    print("Sorry but the wind speed is too small")

elif (t_a < -58 or t_a > 41):
    print("Sorry but the temperature is out of range")

