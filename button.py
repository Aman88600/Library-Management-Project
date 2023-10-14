from tkinter import *

root = Tk()

def myClick():
    # Create the message label when the button is clicked
    message = Label(root, text="Button is clicked")
    # Put the label on the window
    message.grid(row = 1, column = 0)

# Creating a label widget
button = Button(root, text="Click", command=myClick, padx = 50)

# Put the widget on the window
button.grid(row = 0, column = 0)

root.mainloop()
