weight1, price1 = eval(input("Enter the weight and price for package 1: "))
weight2, price2 = eval(input("Enter the weight and price for package 2: "))

ratio1 = price1 / weight1
ratio2 = price2 / weight2


if ratio1 > ratio2:
    print("Package 1 has the better price.")
else:
    print("Package 2 has the better price.")
