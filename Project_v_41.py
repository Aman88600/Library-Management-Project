import sqlite3
import datetime
try:
    con = sqlite3.connect("Library_Management.db")
    cur = con.cursor()

    keep_going = 1
    while (keep_going == 1):
        # Creating option to add book
        user_choice = int(input("""
        Enter 1 to Add book 
        Enter 2 to delete book
        Enter 3 to see all books
        Enter 4 to issue book
        Enter 5 to Add Member:
        Enter 6 to Delete Member
        Enter 7 to See all Members
        Enter 8 to See all the records"""))

        if (user_choice == 1):
            book_name = input("Enter Book name: ")
            book_quantity = int(input("Enter Book quantity: "))
            cur.execute("INSERT INTO Books (Name, Quantity) VALUES (?, ?, ?)", (book_name, book_quantity, 0))
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

        elif (user_choice == 4):
            book_name = str(input("Enter Book name: "))
            Member_name = str(input("Enter member name:"))
            # Searching if the member exists
            Member_exists = 0
            for i in cur.execute("SELECT * FROM Members"):
                if Member_name == i[0]:
                    # print(f"Member exists")
                    Member_exists = 1 
            if Member_exists == 1:
                res = cur.execute(f"SELECT Quantity FROM Books WHERE Name = '{book_name}'")
                new_q = res.fetchall()
                new_qunatity = int(new_q[0][0])
                new_qunatity -= 1
                cur.execute(f"UPDATE Books SET Quantity = {new_qunatity} WHERE Name = '{book_name}'")
                cur.execute("INSERT INTO Records (Book_Name, Member_Name, Issue_time) VALUES (?, ?, ?)", (book_name, Member_name, datetime.datetime.now()))
                con.commit()  # Commit changes to the database
            else:
                print(f"Issue Cancelled, Member doesn't exist")
            res = cur.execute("SELECT * FROM Books")
            print(res.fetchall())
        

        elif (user_choice == 5):
            Member_name = input("Enter new Member name : ")
            cur.execute("INSERT INTO Members (Name) VALUES (?);", (Member_name,))
            con.commit()  # Commit changes to the database
            res = cur.execute("SELECT * FROM Members")
            print(res.fetchall())

        elif(user_choice == 6):
            Member_name = str(input("Enter Member name: "))
            cur.execute(f"DELETE FROM Members WHERE Name = '{Member_name}'")
            con.commit()  # Commit changes to the database
            res = cur.execute("SELECT * FROM Members")
            print(res.fetchall())

        elif (user_choice == 7):
            res = cur.execute("SELECT * FROM Members")
            print(res.fetchall())

        elif (user_choice == 8):
            res = cur.execute("SELECT * FROM Records")
            print(res.fetchall())
        keep_going = int(input("Enter 1 to continue 0 to exit : "))
except sqlite3.Error as e:
    print("SQLite error:", e)

finally:
    con.close()
