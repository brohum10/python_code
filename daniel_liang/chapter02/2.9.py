t_a = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
v = eval(input("Enter the wind speed in miles per hour: "))

if v >= 2:  
    t_wc = 35.74 + (0.6215 * t_a) - (35.75 * (v ** 0.16)) + (0.4275 * t_a * (v ** 0.16))
    print("The wind chill is index is %.5f" %t_wc)
    
else :
    print("Improper input. Input must be bigger or equal to 2.")
