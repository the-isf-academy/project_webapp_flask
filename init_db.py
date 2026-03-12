# You may use this file to reset your database
#   - delete the database.db file
#   - run init_db.py


import sqlite3

# connect to database
connection = sqlite3.connect('database.db')

# open fortune.sql 
with open('colors.sql') as file:
    connection.executescript(file.read())

# close database
connection.close()

print("-- database initalized --")