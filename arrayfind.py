array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
val_1 = int(input("Choose a number from 0-9 to find:"))

d=0
c=0
while c== 0:
    if array[d] == val_1:
        d = str(d)
        print("array[" + d + "]")
        break

    d = d+1
    c= int(input("Press '0' to continue, else type any number."))
