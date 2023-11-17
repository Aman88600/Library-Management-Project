import sqlite3

try:
    con = sqlite3.connect("Library_Management.db")
    cur = con.cursor()

    keep_going = 1
    while (keep_going == 1):
        # Creating option to add book
        user_choice = int(input("""
        Enter 1 to Add book 
        Enter 2 to delete book
        Enter 3 to see all books : """))

        if (user_choice == 1):
            book_name = input("Enter Book name: ")
            book_quantity = int(input("Enter Book quantity: "))
            cur.execute("INSERT INTO Books (Name, Quantity) VALUES (?, ?)", (book_name, book_quantity))
            con.commit()  # Commit changes to the database
            res = cur.execute("SELECT * FROM Books")
            print(res.fetchall())

        elif(user_choice == 2):
            book_name = str(input("Enter Book name: "))
            cur.execute(f"DELETE FROM Books WHERE Name = '{book_name}'")
            con.commit()  # Commit changes to the database
            res = cur.execute("SELECT * FROM Books")
            print(res.fetchall())

        elif (user_choice == 3):
            res = cur.execute("SELECT * FROM Books")
            print(res.fetchall())
        keep_going = int(input(f"Enter 1 to continue 0 to exit : "))
except sqlite3.Error as e:
    print("SQLite error:", e)

finally:
    con.close()
