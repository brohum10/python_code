pounds = eval(input("Enter weight in pounds: "))
inches = eval(input("Enter height in inches: "))

kilos = 0.45359237*pounds
meters = 0.0254*inches

B_M_I = kilos/(meters**2)

print("BMI is %.4f" %B_M_I)
