ratio = eval(input("Enter the exchange rate from dollars to RMB: "))
conversion = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

if conversion == 0:
    USD = eval(input("Enter the dollar amount: "))
    RMB = ratio * USD
    print("$", USD, "is", RMB, "yuan")
elif conversion == 1:
    RMB = eval(input("Enter the Chinese Renminbi amount: "))
    USD = RMB / ratio
    print(RMB, "yuan is", "$", USD)
