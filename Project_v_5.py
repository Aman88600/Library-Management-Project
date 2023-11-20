from tkinter import *
import sqlite3
import datetime

con = sqlite3.connect("Library_Management.db")
cur = con.cursor()

# Avaliable books
def See_Avaliable_Books():
    # Getting data
    res = cur.execute("SELECT * FROM Books")
    records_data = res.fetchall()

    # Create a new window
    See_Avaliable_Books_window = Toplevel(root)
    See_Avaliable_Books_window.geometry("500x500")

    # Specify Grid for the new window
    Grid.rowconfigure(See_Avaliable_Books_window, 0, weight=1)

    # Create labels for each record
    for i, record in enumerate(records_data):
        record_label = Label(See_Avaliable_Books_window, text=f"Record {i + 1}: {record}")
        record_label.grid(row=i, column=0, sticky="W", pady=5, padx=10)

        # Adjust the grid row configuration for each label
        Grid.rowconfigure(See_Avaliable_Books_window, i, weight=1)

    # Adjust column weight to allow the labels to expand horizontally
    Grid.columnconfigure(See_Avaliable_Books_window, 0, weight=1)

# See all members
# def see_all_members():

#     # Getting data  
#     res = cur.execute("SELECT * FROM Members")
#     records_data = res.fetchall()

#     # Create a new window
#     See_Avaliable_Member_window = Toplevel(root)
#     See_Avaliable_Member_window.geometry("500x500")

def create_books_window():
    books_window = Toplevel(root)
    books_window.geometry("500x500")

    # Specify Grid for the new window
    Grid.rowconfigure(books_window, 0, weight=1)
    Grid.columnconfigure(books_window, 0, weight=1)

    Grid.rowconfigure(books_window, 1, weight=1)
    Grid.rowconfigure(books_window, 2, weight=1)

    # Create new Buttons on the new window
    See_Books = Button(books_window, text="See Available Books", command=See_Avaliable_Books)
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

    Grid.rowconfigure(members_window, 1, weight=1)
    Grid.rowconfigure(members_window, 2, weight=1)

    # Create new Buttons on the new window
    See_Members = Button(members_window, text="See Current Members")
    See_Members.grid(row=0, column=0, sticky="NSEW")

    Add_Member = Button(members_window, text="Add Member")
    Add_Member.grid(row=1, column=0, sticky="NSEW")

    Delete_Member = Button(members_window, text="Delete Member")
    Delete_Member.grid(row=2, column=0, sticky="NSEW")


def records_function():
    # Getting data
    res = cur.execute("SELECT * FROM Records")
    records_data = res.fetchall()

    # Create a new window
    records_window = Toplevel(root)
    records_window.geometry("500x500")

    # Specify Grid for the new window
    Grid.rowconfigure(records_window, 0, weight=1)

    # Create labels for each record
    for i, record in enumerate(records_data):
        record_label = Label(records_window, text=f"Record {i + 1}: {record}")
        record_label.grid(row=i, column=0, sticky="W", pady=5, padx=10)

        # Adjust the grid row configuration for each label
        Grid.rowconfigure(records_window, i, weight=1)

    # Adjust column weight to allow the labels to expand horizontally
    Grid.columnconfigure(records_window, 0, weight=1)




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
Records = Button(root, text="Records", command=records_function)

# Set grid
Books.grid(row=0, column=0, sticky="NSEW")
Members.grid(row=1, column=0, sticky="NSEW")
Records.grid(row=2, column=0, sticky="NSEW")

# Execute tkinter
root.mainloop()
