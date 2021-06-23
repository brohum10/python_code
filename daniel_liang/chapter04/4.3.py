a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

no_sol = ((a*d) - (b*c))




if no_sol == 0:
    print("The equation has no solutions")
else:
    x = (e*d - b*f) / (no_sol)
    y = (a*f - e*c)/ (no_sol)
    print("x is", float(x), "and y is", float(y))
