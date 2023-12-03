import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Library_Management.db')
cursor = conn.cursor()

# Define SQL statements to drop tables if they exist
drop_books_table = "DROP TABLE IF EXISTS Books;"
drop_members_table = "DROP TABLE IF EXISTS Members;"
drop_records_table = "DROP TABLE IF EXISTS Records;"

# Execute the SQL statements to drop tables
cursor.execute(drop_books_table)
cursor.execute(drop_members_table)
cursor.execute(drop_records_table)

# Define SQL statements to create tables
create_books_table = """
CREATE TABLE Books (
    Name varchar(30),
    Quantity int,
    Issued int
);
"""

create_members_table = """
CREATE TABLE Members (
    Name varchar(30)
);
"""

create_records_table = """
CREATE TABLE Records (
    Book_Name varchar(30),
    Member_Name varchar(30),
    Issue_time timestamp,
    Action varchar(20),
    Fine float
);
"""


# Execute the SQL statements to create tables
cursor.execute(create_books_table)
cursor.execute(create_members_table)
cursor.execute(create_records_table)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Tables deleted and recreated successfully.")
