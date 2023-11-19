from tkinter import *

root = Tk()
root.geometry("500x500")

# Specify Grid
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)

# Functions
# Books
def Books_function():
    # Destroy the original buttons
    Books.destroy()
    Members.destroy()
    Records.destroy()

    # Create new Buttons
    # See Books
    See_Books = Button(root, text="See Available Books", command=see_books_function)
    See_Books.grid(row=0, column=0, sticky="NSEW")

    # Add Books
    Add_Book = Button(root, text="Add Book")
    Add_Book.grid(row=1, column=0, sticky="NSEW")

    # Delete Book
    Delete_Book = Button(root,text="Delete Book")
    Delete_Book.grid(row=2, column=0, sticky="NSEW")

# Members
def Members_function():
    # Destroy the original buttons
    Books.destroy()
    Members.destroy()
    Records.destroy()

    # Create new Buttons
    # See Members
    See_Members = Button(root, text="See Current Members")
    See_Members.grid(row=0, column=0, sticky="NSEW")

    # Add Members
    Add_Member = Button(root, text="Add Member")
    Add_Member.grid(row=1, column=0, sticky="NSEW")

    # DeleteMembers
    Delete_Member = Button(root,text="Delete Member")
    Delete_Member.grid(row=2, column=0, sticky="NSEW")

# See Books function
def see_books_function():
    # Create a new window or perform any other functionality
    new_window = Toplevel(root)
    new_window.geometry("300x200")
    label = Label(new_window, text="List of Available Books")
    label.pack()

# Create Buttons
Books = Button(root, text="Books", command=Books_function)
Members = Button(root, text="Members", command=Members_function)
Records = Button(root, text="Records")

# Set grid
Books.grid(row=0, column=0, sticky="NSEW")
Members.grid(row=1, column=0, sticky="NSEW")
Records.grid(row=2, column=0, sticky="NSEW")

# Execute tkinter
root.mainloop()
