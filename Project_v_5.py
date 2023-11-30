from tkinter import *
from tkinter import simpledialog,messagebox
import sqlite3
import datetime

con = sqlite3.connect("Library_Management.db")
cur = con.cursor()


# See Avaliable Books
def See_Books_function():
    See_Books_window = Toplevel(root)
    See_Books_window.geometry("500x500")

    # Get all the books from the database
    all_books_data = cur.execute("SELECT * FROM Books")
    # Making data readable
    all_books_data_readable = all_books_data.fetchall()
    # Option 1
    counter = 0
    Grid.columnconfigure(See_Books_window, 0, weight=1)
    for i in all_books_data_readable:
        Grid.rowconfigure(See_Books_window, int(counter), weight=1)
        first_book = Label(See_Books_window, text=f"Name : {i[0]}, Quantity : {i[1]}, Issued : {i[2]}")
        first_book.grid(row = int(counter), column = 0, sticky = "NSEW")
        counter += 1
    # Option 2
    # Grid.columnconfigure(See_Books_window, 0, weight=1)
    # Grid.rowconfigure(See_Books_window, 0, weight=1)
    # Grid.rowconfigure(See_Books_window, 1, weight=1)
    # book_name_lable = Label(See_Books_window, text="Search For Books")
    # book_name_lable.grid(row = 0, column = 0, sticky = "NSEW")
    # book_name = Entry(See_Books_window)
    # book_name.grid(row = 0, column = 1, sticky = "NSEW")




def issue_book_function():
    # Create a Toplevel window for input
    input_window = Toplevel()
    input_window.title("Issue Book")
    input_window.geometry("300x120")

    # Create labels and entry widgets for book and member names
    label_book = Label(input_window, text="Book Name:")
    label_book.grid(row=0, column=0, padx=10, pady=5, sticky="E")

    entry_book = Entry(input_window)
    entry_book.grid(row=0, column=1, padx=10, pady=5, sticky="W")

    label_member = Label(input_window, text="Member Name:")
    label_member.grid(row=1, column=0, padx=10, pady=5, sticky="E")

    entry_member = Entry(input_window)
    entry_member.grid(row=1, column=1, padx=10, pady=5, sticky="W")

    # Function to handle book issuance
    def issue_book():
        book_name = entry_book.get()
        member_name = entry_member.get()

        if book_name and member_name:
            # Check if the book is available
            cur.execute("SELECT * FROM Books WHERE name=? AND quantity>0", (book_name,))
            available_book = cur.fetchone()

            if available_book:
                # Update the Books table
                cur.execute("UPDATE Books SET quantity = quantity - 1, Issued = Issued + 1 WHERE name=?", (book_name,))
                con.commit()

                # Update the Records table
                current_time = datetime.datetime.now()
                cur.execute("INSERT INTO Records (Book_Name, Member_Name, Issue_time, Action) VALUES (?, ?, ?, ?)",
                            (book_name, member_name, current_time, "Issue"))
                con.commit()

                messagebox.showinfo("Success", f"{book_name} issued to {member_name} successfully!")
                input_window.destroy()
            else:
                messagebox.showwarning("Warning", f"{book_name} is not available for issuance.")
        else:
            messagebox.showwarning("Warning", "Both book name and member name are required.")

    # Create a button to execute the issuance
    issue_button = Button(input_window, text="Issue Book", command=issue_book)
    issue_button.grid(row=2, column=0, columnspan=2, pady=10)

    input_window.mainloop()

# Add Book
def Add_Book_function():
    Add_Book_window = Toplevel(root)
    Add_Book_window.geometry("300x150")

    # Create labels and entry widgets
    label_name = Label(Add_Book_window, text="Book Name:")
    label_name.grid(row=0, column=0, pady=5, padx=10, sticky="E")

    entry_name = Entry(Add_Book_window)
    entry_name.grid(row=0, column=1, pady=5, padx=10, sticky="W")

    label_quantity = Label(Add_Book_window, text="Quantity:")
    label_quantity.grid(row=1, column=0, pady=5, padx=10, sticky="E")

    entry_quantity = Entry(Add_Book_window)
    entry_quantity.grid(row=1, column=1, pady=5, padx=10, sticky="W")

    # Function to add book to the database
    def add_book_to_database():
        book_name = entry_name.get()
        book_quantity = entry_quantity.get()

        if book_name and book_quantity:
            # Insert the book into the database
            cur.execute("INSERT INTO Books (name, quantity, Issued) VALUES (?, ?, ?)", (book_name, book_quantity, 0))
            con.commit()
            messagebox.showinfo("Success", "Book added successfully!")
            Add_Book_window.destroy()
        else:
            messagebox.showwarning("Warning", "Book name and quantity are required.")

    # Create a button to execute the function
    add_button = Button(Add_Book_window, text="Add Book", command=add_book_to_database)
    add_button.grid(row=2, column=0, columnspan=2, pady=10)


def Delete_Book_function():
    Delete_Book_window = Toplevel(root)
    Delete_Book_window.geometry("300x150")

    # Create labels and entry widgets
    label_name = Label(Delete_Book_window, text="Book Name:")
    label_name.grid(row=0, column=0, pady=5, padx=10, sticky="E")

    entry_name = Entry(Delete_Book_window)
    entry_name.grid(row=0, column=1, pady=5, padx=10, sticky="W")

    # Function to delete book from the database
    def delete_book_from_database():
        book_name = entry_name.get()

        if book_name:
            # Check if the book exists in the database
            cur.execute("SELECT * FROM Books WHERE name=?", (book_name,))
            existing_book = cur.fetchone()

            if existing_book:
                # Delete the book from the database
                cur.execute("DELETE FROM Books WHERE name=?", (book_name,))
                con.commit()
                messagebox.showinfo("Success", "Book deleted successfully!")
                Delete_Book_window.destroy()
            else:
                messagebox.showwarning("Warning", f"Book with name '{book_name}' not found.")
        else:
            messagebox.showwarning("Warning", "Book name is required.")

    # Create a button to execute the function
    delete_button = Button(Delete_Book_window, text="Delete Book", command=delete_book_from_database)
    delete_button.grid(row=1, column=0, columnspan=2, pady=10)




def create_books_window():
    books_window = Toplevel(root)
    books_window.geometry("500x500")

    # Specify Grid for the new window
    Grid.rowconfigure(books_window, 0, weight=1)
    Grid.columnconfigure(books_window, 0, weight=1)

    Grid.rowconfigure(books_window, 1, weight=1)
    Grid.rowconfigure(books_window, 2, weight=1)
    Grid.rowconfigure(books_window, 3, weight=1)

    # Create new Buttons on the new window
    See_Books = Button(books_window, text="See Available Books", command=See_Books_function)
    See_Books.grid(row=0, column=0, sticky="NSEW")

    Add_Book = Button(books_window, text="Add Book", command=Add_Book_function)
    Add_Book.grid(row=1, column=0, sticky="NSEW")

    Delete_Book = Button(books_window, text="Delete Book", command=Delete_Book_function)
    Delete_Book.grid(row=2, column=0, sticky="NSEW")

    Issue_book = Button(books_window, text="Issue Book", command=issue_book_function)
    Issue_book.grid(row=3, column=0, sticky="NSEW")







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
