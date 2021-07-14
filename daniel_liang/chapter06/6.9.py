meters = 20
def feetToMeter(meters):
    
    print("Feet \t Meters")

    for feet in range(1, 11, 1):
        meters = feet * 0.305
        print(feet ,"\t %.3f"  %meters)


def meterToFeet(meters):
    
    print("Meters \t Feet")

    for meters in range(20, 72, 6):
        feet = meters / 0.305
        print(meters ,"\t %.3f"  %feet)

feetToMeter(meters)
print("- -- -- -- -")
meterToFeet(meters)
