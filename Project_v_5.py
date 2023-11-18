# A GUI App for Library management 
from tkinter import *

root = Tk()

# Setting the title
root.title("Libaray")
# Setting the initial size
root.geometry("200x200")
# root.iconbitmap('icons8-library-50.png')
# Creating Books button
Books = Button(root, text="Books", padx=50)
# Putting book button on the screen
Books.grid(row=0, column=0)

# Creating Members Button
Members = Button(root, text="Members", padx=50)
# Putting button on the screen
Members.grid(row=1, column=0)

# Creating Records Button 
Records = Button(root, text = "Records", padx=50)
# Putting Records button on the screen
Records.grid(row=2, column=0)

root.mainloop()