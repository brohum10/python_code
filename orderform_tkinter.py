import tkinter
import tkinter.simpledialog
import tkinter.messagebox

root = tkinter.Tk()
w = tkinter.Label(root, text="Dialog Practice")
w.pack()
tkinter.messagebox.showinfo("Welcome", "Welcome to Zippy Inc.!, enter anything in the box below to continue your order")
name = tkinter.simpledialog.askstring("name", "Please enter your full name")
item1 = tkinter.simpledialog.askstring("item1", "Please enter your order item")
tkinter.messagebox.showinfo ("Stock", "It's your lucky day, that item is in stock today! We will now proceed to ask your shipping address!")
street = tkinter.simpledialog.askstring("street", "Please enter your street")
city = tkinter.simpledialog.askstring("city", "Please enter your city")
state = tkinter.simpledialog.askstring("state", "Please enter your state")
zipcode = tkinter.simpledialog.askstring("zipcode", "Please enter your zipcode")

Shippingaddress=(street + " " + city + ", " + state + " "+ zipcode)
yandn = tkinter.simpledialog.askstring("yandn", "We a required to ask if your billing address and shipping address are the same. Please enter y for yes or n for no. Please note: be careful when typing your letter.")

if yandn=="y":

    tkinter.messagebox.showinfo("Order Summary", "Order Summary for " + name + "\nShipping Address:\n" + name + Shippingaddress + "\n\n\n" + "\nBilling Address:\n" + "Same As Shipping Address" + "\n\n" + "Items:\n" + item1)
    tkinter.messagebox.showinfo("THANKS", "Thankyou for your order, your order should be arriving in a zippy!")
    
if yandn=="n":

    street2 = tkinter.simpledialog.askstring("street", "Please enter the street")
    city2 = tkinter.simpledialog.askstring("city", "Please enter the city")
    state2 = tkinter.simpledialog.askstring("state", "Please enter the state")
    zipcode2 = tkinter.simpledialog.askstring("zipcode", "Please enter the zipcode")

    tkinter.messagebox.showinfo("Order Summary", "Order Summary for " + name + "\nShipping Address:\n" + name +  Shippingaddress +  "\n\n\n" + "\nBilling Address:\n" + name2 + "\n" + street2 + " " + city2 + ", " + state2 + " "
    + zipcode2 + "\n\n" + "Items:\n" + item1)
    tkinter.messagebox.showinfo("THANKS", "Thankyou for your order, your order should be arriving in a zippy!")

else:

    yandn = tkinter.simpledialog.askstring("yandn", "Try again one more time.")

    if yandn=="y":

        tkinter.messagebox.showinfo("Order Summary", "Order Summary for " + name + "\nShipping Address:\n" + name + Shippingaddress + "\n\n\n" + "\nBilling Address:\n" + "Same As Shipping Address" + "\n\n" + "Items:\n" + item1)
        tkinter.messagebox.showinfo("THANKS", "Thankyou for your order, your order should be arriving in a zippy!")
        
    if yandn=="n":

        street2 = tkinter.simpledialog.askstring("street", "Please enter the street")
        city2 = tkinter.simpledialog.askstring("city", "Please enter the city")
        state2 = tkinter.simpledialog.askstring("state", "Please enter the state")
        zipcode2 = tkinter.simpledialog.askstring("zipcode", "Please enter the zipcode")

        tkinter.messagebox.showinfo("Order Summary", "Order Summary for " + name + "\nShipping Address:\n" + name +  Shippingaddress +  "\n\n\n" + "\nBilling Address:\n" + name2 + "\n" + street2 + " " + city2 + ", " + state2 + " " + zipcode2 + "\n\n" + "Items:\n" + item1)
        tkinter.messagebox.showinfo("THANKS", "Thankyou for your order, your order should be arriving in a zippy!")
            
    else:

        tkinter.messagebox.showinfo("yandn", "Goodbye")
