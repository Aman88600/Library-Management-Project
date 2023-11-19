from tkinter import *

def create_books_window():
    books_window = Toplevel(root)
    books_window.geometry("500x500")

    # Specify Grid for the new window
    Grid.rowconfigure(books_window, 0, weight=1)
    Grid.columnconfigure(books_window, 0, weight=1)

    Grid.rowconfigure(books_window, 1, weight=1)
    Grid.rowconfigure(books_window, 2, weight=1)

    # Create new Buttons on the new window
    See_Books = Button(books_window, text="See Available Books")
    See_Books.grid(row=0, column=0, sticky="NSEW")

    Add_Book = Button(books_window, text="Add Book")
    Add_Book.grid(row=1, column=0, sticky="NSEW")

    Delete_Book = Button(books_window, text="Delete Book")
    Delete_Book.grid(row=2, column=0, sticky="NSEW")

def create_members_window():
    members_window = Toplevel(root)
    members_window.geometry("500x500")

    # Specify Grid for the new window
    Grid.rowconfigure(members_window, 0, weight=1)
    Grid.columnconfigure(members_window, 0, weight=1)

    # Create new Buttons on the new window
    See_Members = Button(members_window, text="See Current Members")
    See_Members.grid(row=0, column=0, sticky="NSEW")

    Add_Member = Button(members_window, text="Add Member")
    Add_Member.grid(row=1, column=0, sticky="NSEW")

    Delete_Member = Button(members_window, text="Delete Member")
    Delete_Member.grid(row=2, column=0, sticky="NSEW")

root = Tk()
root.geometry("500x500")

# Specify Grid
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)

# Create Buttons
Books = Button(root, text="Books", command=create_books_window)
Members = Button(root, text="Members", command=create_members_window)
Records = Button(root, text="Records")

# Set grid
Books.grid(row=0, column=0, sticky="NSEW")
Members.grid(row=1, column=0, sticky="NSEW")
Records.grid(row=2, column=0, sticky="NSEW")

# Execute tkinter
root.mainloop()
