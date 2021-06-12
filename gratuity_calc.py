sub_total = float(input("Enter a sub total. Ex; 10.5, 12, 201:\n"))
g_rate = float(input("Enter gratuity rate/precent: Ex; 1.5, 2, 15\n"))

add_on = float(sub_total * (g_rate/100) )

print(str(add_on) , " is the gratuity.")

gratuity = float(add_on + sub_total)

print(str(gratuity), " is the total.")
