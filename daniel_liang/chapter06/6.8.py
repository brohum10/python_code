f = 120
def ctof(f):
    
    print("Celsius \t Fahrenheit")

    for c in range(40, 30, -1):
        f = ((9/5) * c) +32
        print(c ,"\t %.1f"  %f)


def ftoc(f):
    
    print("Fahrenheit \t Celsius")

    for f in range(120, 20, -10):
        c = (5/9) * (f - 32)
        print(f ,"\t %.3f"  %c)

ctof(f)
print("- -- -- -- -")
ftoc(f)
