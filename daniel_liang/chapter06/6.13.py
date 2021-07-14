def sum_series(x):
    
    #total is a variable storing the sum of the series
    total=0
    
    #running a for loop for 'x' number of times
    for i in range(1, x+1):
        
        #computing the sum by the given formula in the question
        total=total+i/(i+1)
    
    #returning the total
    return total
    
#main function    
def main():
    
    #printing the index for the table
    print("i      m(i)")
    
    #running a for loop for the first 20 elements in the series
    for x in range(1,21):
        
        #calling the function sum_series and passing the argument
        #and printing the returned value.
        #The str function converts interger values into string
        print(str(x)+"      "+ str(sum_series(x)))

#calling the main function        
main()
