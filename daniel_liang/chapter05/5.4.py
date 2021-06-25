miles = 1
print("MIles \t Kilorgams")

for miles in range(1, 200, 2):
    kilometers = miles * 1.609
    print(str(format(miles, "<4.0f")) + str(format(kilometers, "20.3f")))
