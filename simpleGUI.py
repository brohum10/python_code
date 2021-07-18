import tkinter as tkn

window = tkn.Tk()
label = tkn.Label(window, text = "welcome to python")
button = tkn.Button(window, text = "Click Me")
label.pack()
button.pack()

window.mainloop()
