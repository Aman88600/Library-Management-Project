import sqlite3

try:
    con = sqlite3.connect("Library_Management.db")
    cur = con.cursor()

    book_name = input("Enter Book name: ")
    book_quantity = int(input("Enter Book quantity: "))

    cur.execute("INSERT INTO Books (Name, Quantity) VALUES (?, ?)", (book_name, book_quantity))

    res = cur.execute("SELECT * FROM Books")
    print(res.fetchall())

    con.commit()  # Commit changes to the database

except sqlite3.Error as e:
    print("SQLite error:", e)

finally:
    con.close()

input("")
