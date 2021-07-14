def sum_series(x):
    
    #total is a variable storing the sum of the series
    total=0
    
    #running a for loop for 'x' number of times
    for i in range(1, x+1):
        
        #computing the sum by the given formula in the question
        total=total+(-1)**(i+1)/(2*i-1)
    
    #returning the total
    #multipling by 4 as given in the formula
    return 4*total
    
#main function    
def main():
    
    #printing the index for the table
    print("i         m(i)")
    
    #running a for loop from 1 to 1000 with step value of 100
    for x in range(1,1000,100):
        
        #calling the function sum_series and passing the argument
        #and printing the returned value
        print(str(x)+"         "+ str(sum_series(x)))

#calling the main function        
main()
