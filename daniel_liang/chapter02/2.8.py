M = eval(input("Enter the amount of water in kilogrames: "))
start_temp = eval(input("Enter the initial temperature: "))
end_temp = eval(input("Enter the final temperature: "))

Q = M * 4184 * (end_temp - start_temp) 

print("The energy needed is ", Q)
