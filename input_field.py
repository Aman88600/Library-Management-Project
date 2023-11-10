from tkinter import *

root = Tk()

# Making the entry field
e = Entry(root)
e.insert(0, "Enter Your Name")
#Putting it on the screen
e.grid(row = 0, column = 0)

def button_function():
    name = e.get()
    msg = Label(root, text =f"Hello, {name}")
    msg.grid(row = 2, column = 0)

# Making the button
button = Button(root, text="Click", command = button_function)
button.grid(row = 1, column = 0)

root.mainloop()