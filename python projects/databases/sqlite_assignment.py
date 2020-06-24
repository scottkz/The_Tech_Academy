# The Tech Academy - Software Developer BootCamp
#
# Python Version: 3.8.3
#
# Author: Scott Katzelnick
#
# Purpose:
#
# SQLITE ASSIGNMENT PARTS ONE THROUGH Eight;

# Import the SQLite3 module
import sqlite3

# Make a connection to a database and declare it to a variable
connection = sqlite3.connect("test_database.db")

# Declaring a variable to instantiate the cursor object
c = connection.cursor()

# Executing SQL statements on the database & applying the changes
c.execute("Create Table If Not Exists People(FirstName Text, LastName Text, Age Int)")
connection.commit()

c.execute("Insert Into People Values('Ron', 'Obvious', 42)")
connection.commit()

# Closing the database to restrict memory leak
connection.close()

# Connecting, running SQL statements and committing changes using executescript()
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.executescript("""Drop Table If Exists People;
                    Create Table People(FirstName Text, LastName Text, Age Int);
                    Insert Into People Values('Ron', 'Obvious', 42);
                    """)
    peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
    c.executemany("Insert Into People Values (?, ?, ?)", peopleValues)

# Getting personal data from users
firstName = input('Enter you first name: ')
lastName = input('Enter your last name: ')
age = int(input("Enter your age: "))

# Executing the SQL Insert statements with supplied data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    line = "Insert Into People Values ('\"?\", \"?\", \"?\"')", (firstName, lastName, str(age))
    c.execute(line)
    connection.close()

# Using placeholders and tuples
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (first_name, last_name, age)

# Using the given data
with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("Insert Into People Values (?, ?, ?)", personData)
    c.execute("Update People Set Age=? Where FirstName=? And LastName=?", (45, 'Luigi', 'Vercotti'))
    c.execute("Select FirstName, LastName From People Where Age >30")
    for row in c.fetchall():
        print(row)




