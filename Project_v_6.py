from tkinter import *
from tkinter import simpledialog, messagebox
import sqlite3
import datetime

con = sqlite3.connect("Library_Management.db")
cur = con.cursor()


def See_Books_function():
    See_Books_window = Toplevel(root)
    See_Books_window.geometry("500x500")

    all_books_data = cur.execute("SELECT * FROM Books")
    all_books_data_readable = all_books_data.fetchall()

    for i, book in enumerate(all_books_data_readable):
        book_frame = Frame(See_Books_window)
        book_frame.grid(row=i, column=0, sticky="NSEW")

        book_label = Label(book_frame, text=f"Name: {book[0]}, Quantity: {book[1]}, Issued: {book[2]}")
        book_label.grid(row=0, column=0, sticky="W")

        issue_button = Button(book_frame, text="Issue Book", command=lambda b=book[0]: issue_book_function(b))
        issue_button.grid(row=0, column=1, padx=5)

        return_button = Button(book_frame, text="Return Book", command=lambda b=book[0]: return_book_function(b))
        return_button.grid(row=0, column=2, padx=5)



def issue_book_function(book_name):
    member_name = simpledialog.askstring("Input", "Enter Member's Name:")

    if member_name:
        # Check if the member is registered
        cur.execute("SELECT * FROM Members WHERE Name=?", (member_name,))
        registered_member = cur.fetchone()

        if registered_member:
            cur.execute("SELECT * FROM Books WHERE name=? AND quantity>0", (book_name,))
            available_book = cur.fetchone()

            if available_book:
                cur.execute("UPDATE Books SET quantity = quantity - 1, Issued = Issued + 1 WHERE name=?", (book_name,))
                con.commit()

                current_time = datetime.datetime.now()
                cur.execute("INSERT INTO Records (Book_Name, Member_Name, Issue_time, Action) VALUES (?, ?, ?, ?)",
                            (book_name, member_name, current_time, "Issue"))
                con.commit()

                messagebox.showinfo("Success", f"{book_name} issued to {member_name} successfully!")
            else:
                messagebox.showwarning("Warning", f"{book_name} is not available for issuance.")
        else:
            messagebox.showwarning("Warning", f"{member_name} is not a registered member. Please register first.")
    else:
        messagebox.showwarning("Warning", "Member's name is required.")


def return_book_function(book_name):
    member_name = simpledialog.askstring("Input", "Enter Member's Name:")

    if member_name:
        # Check if the member is registered
        cur.execute("SELECT * FROM Members WHERE Name=?", (member_name,))
        registered_member = cur.fetchone()

        if registered_member:
            cur.execute("SELECT * FROM Records WHERE Book_Name=? AND Member_Name=? AND Action='Issue'",
                        (book_name, member_name))
            issued_record = cur.fetchone()

            if issued_record:
                cur.execute("UPDATE Books SET quantity = quantity + 1, Issued = Issued - 1 WHERE name=?", (book_name,))
                con.commit()

                current_time = datetime.datetime.now()
                issue_time = datetime.datetime.strptime(issued_record[2], "%Y-%m-%d %H:%M:%S.%f")

                # Calculate the fine based on the duration
                duration = current_time - issue_time
                fine = 1 + max(0, (duration.days - 1))  # $1 for default, $1 for each day after

                cur.execute("INSERT INTO Records (Book_Name, Member_Name, Issue_time, Action, Fine) VALUES (?, ?, ?, ?, ?)",
                            (book_name, member_name, current_time, "Return", fine))
                con.commit()

                messagebox.showinfo("Success", f"{book_name} returned by {member_name} successfully!\nFine: ${fine}")
            else:
                messagebox.showwarning("Warning", f"{book_name} is not issued to {member_name}.")
        else:
            messagebox.showwarning("Warning", f"{member_name} is not a registered member. Please register first.")
    else:
        messagebox.showwarning("Warning", "Member's name is required.")





def Add_Book_function():
    Add_Book_window = Toplevel(root)
    Add_Book_window.geometry("300x150")

    label_name = Label(Add_Book_window, text="Book Name:")
    label_name.grid(row=0, column=0, pady=5, padx=10, sticky="E")

    entry_name = Entry(Add_Book_window)
    entry_name.grid(row=0, column=1, pady=5, padx=10, sticky="W")

    label_quantity = Label(Add_Book_window, text="Quantity:")
    label_quantity.grid(row=1, column=0, pady=5, padx=10, sticky="E")

    entry_quantity = Entry(Add_Book_window)
    entry_quantity.grid(row=1, column=1, pady=5, padx=10, sticky="W")

    def add_book_to_database():
        book_name = entry_name.get()
        book_quantity = entry_quantity.get()

        if book_name and book_quantity:
            cur.execute("INSERT INTO Books (name, quantity, Issued) VALUES (?, ?, ?)", (book_name, book_quantity, 0))
            con.commit()
            messagebox.showinfo("Success", "Book added successfully!")
            Add_Book_window.destroy()
        else:
            messagebox.showwarning("Warning", "Book name and quantity are required.")

    add_button = Button(Add_Book_window, text="Add Book", command=add_book_to_database)
    add_button.grid(row=2, column=0, columnspan=2, pady=10)


def Delete_Book_function():
    Delete_Book_window = Toplevel(root)
    Delete_Book_window.geometry("300x150")

    label_name = Label(Delete_Book_window, text="Book Name:")
    label_name.grid(row=0, column=0, pady=5, padx=10, sticky="E")

    entry_name = Entry(Delete_Book_window)
    entry_name.grid(row=0, column=1, pady=5, padx=10, sticky="W")

    def delete_book_from_database():
        book_name = entry_name.get()

        if book_name:
            cur.execute("SELECT * FROM Books WHERE name=?", (book_name,))
            existing_book = cur.fetchone()

            if existing_book:
                cur.execute("DELETE FROM Books WHERE name=?", (book_name,))
                con.commit()
                messagebox.showinfo("Success", "Book deleted successfully!")
                Delete_Book_window.destroy()
            else:
                messagebox.showwarning("Warning", f"Book with name '{book_name}' not found.")
        else:
            messagebox.showwarning("Warning", "Book name is required.")

    delete_button = Button(Delete_Book_window, text="Delete Book", command=delete_book_from_database)
    delete_button.grid(row=1, column=0, columnspan=2, pady=10)


def create_books_window():
    books_window = Toplevel(root)
    books_window.geometry("500x500")

    Grid.rowconfigure(books_window, 0, weight=1)
    Grid.columnconfigure(books_window, 0, weight=1)

    Grid.rowconfigure(books_window, 1, weight=1)
    Grid.rowconfigure(books_window, 2, weight=1)

    See_Books = Button(books_window, text="See Available Books", command=See_Books_function)
    See_Books.grid(row=0, column=0, sticky="NSEW")

    Add_Book = Button(books_window, text="Add Book", command=Add_Book_function)
    Add_Book.grid(row=1, column=0, sticky="NSEW")

    Delete_Book = Button(books_window, text="Delete Book", command=Delete_Book_function)
    Delete_Book.grid(row=2, column=0, sticky="NSEW")






def add_member_function():
    Add_Member_window = Toplevel(root)
    Add_Member_window.geometry("300x150")

    label_name = Label(Add_Member_window, text="Member Name:")
    label_name.grid(row=0, column=0, pady=5, padx=10, sticky="E")

    entry_name = Entry(Add_Member_window)
    entry_name.grid(row=0, column=1, pady=5, padx=10, sticky="W")

    def add_member_to_database():
        member_name = entry_name.get()

        if member_name:
            cur.execute("INSERT INTO Members (Name) VALUES (?)", (member_name,))
            con.commit()
            messagebox.showinfo("Success", f"Member {member_name} added successfully!")
            Add_Member_window.destroy()
        else:
            messagebox.showwarning("Warning", "Member name is required.")

    add_button = Button(Add_Member_window, text="Add Member", command=add_member_to_database)
    add_button.grid(row=1, column=0, columnspan=2, pady=10)


def See_Members_function():
    See_Members_window = Toplevel(root)
    See_Members_window.geometry("500x500")

    all_members_data = cur.execute("SELECT * FROM Members")
    all_members_data_readable = all_members_data.fetchall()

    for i, member in enumerate(all_members_data_readable):
        member_frame = Frame(See_Members_window)
        member_frame.grid(row=i, column=0, sticky="NSEW")

        member_label = Label(member_frame, text=f"Name: {member[0]}")
        member_label.grid(row=0, column=0, sticky="W")

        delete_button = Button(member_frame, text="Delete Member", command=lambda m=member[0]: delete_member_function(m))
        delete_button.grid(row=0, column=1, padx=5)


def delete_member_function(member_name):
    confirm = messagebox.askyesno("Confirm", f"Do you want to delete member {member_name}?")
    if confirm:
        cur.execute("DELETE FROM Members WHERE Name=?", (member_name,))
        con.commit()
        messagebox.showinfo("Success", f"Member {member_name} deleted successfully.")


def create_members_window():
    members_window = Toplevel(root)
    members_window.geometry("500x500")

    Grid.rowconfigure(members_window, 0, weight=1)
    Grid.columnconfigure(members_window, 0, weight=1)

    Grid.rowconfigure(members_window, 1, weight=1)
    See_Members = Button(members_window, text="See Current Members", command=See_Members_function)
    See_Members.grid(row=0, column=0, sticky="NSEW")

    Add_Member = Button(members_window, text="Add Member", command=add_member_function)
    Add_Member.grid(row=1, column=0, sticky="NSEW")


def records_function():
    res = cur.execute("SELECT * FROM Records")
    records_data = res.fetchall()

    records_window = Toplevel(root)
    records_window.geometry("500x500")

    Grid.rowconfigure(records_window, 0, weight=1)

    for i, record in enumerate(records_data):
        record_label = Label(records_window, text=f"Record {i + 1}: {record}")
        record_label.grid(row=i, column=0, sticky="W", pady=5, padx=10)

        Grid.rowconfigure(records_window, i, weight=1)

    Grid.columnconfigure(records_window, 0, weight=1)


root = Tk()
root.geometry("500x500")

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)

Books = Button(root, text="Books", command=create_books_window)
Members = Button(root, text="Members", command=create_members_window)
Records = Button(root, text="Records", command=records_function)

Books.grid(row=0, column=0, sticky="NSEW")
Members.grid(row=1, column=0, sticky="NSEW")
Records.grid(row=2, column=0, sticky="NSEW")

root.mainloop()
