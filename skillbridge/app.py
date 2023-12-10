# Read and execute the entities.sql file to create the sqlite database and tables for the application.

import os
import sqlite3

db_path = os.path.join(os.path.dirname(__file__), 'skillbridge.db')

# Connect to the database
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Read the entities.sql file

f = open('entities.sql', 'r')
sql = f.read()
f.close()

# Execute the sql commands

c.executescript(sql)

f = open('seed-data.sql', 'r')
sql = f.read()
f.close()

c.executescript(sql)


# Close the connection

conn.close()

print("Database created successfully.")
