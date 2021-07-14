#Defining the function 'printChars'
def printChars(ch1, ch2, numberPerLine):
    
    #y is a variable storing the count of 
    #elements printed on the screen
    #as we have to print only a given number of characters per line
    y=0
    
    #Running a for loop
    #'ord' function returns the ASCII value of the character
    #Thus, Running the loop from the ASCII value of the starting character to
    #the ASCII value of the last character
    for x in range(ord(ch1),ord(ch2)+1):
        
        #incrementing y by 1
        y+=1
        
        
        #checking if the limit of character to be printed
        #per line is reached or not
        if(y%numberPerLine==0):
            
            #printing the character
            #the 'chr' function converts the ASCII value back to character
            print(chr(x))
            
        else:
            
            #else printing the character with a " " at the end
            print(chr(x), end=" ")
            
        
            
def main():
    
    #Calling the printChars function and passing the arguments
    printChars("I", "Z",10)

#Calling the main function
main()
