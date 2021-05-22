char_lett = input("Enter some characters.")

d=0
g = -1
c = 0
while c < len(char_lett)/2:
    
    if char_lett[0+d] == char_lett[(len(char_lett))+g]:
        print("palindrome")
    else:
        print("not palindrome")
        break
    c = c +1
    d = d+1
    g = g -1

print(len(char_lett))
