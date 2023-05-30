import sqlite3

#connecting with the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

#create a query to build a table if it doesn't exist
create_table_query = '''CREATE TABLE IF NOT EXISTS employee(employee_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, designation TEXT, salary REAL)'''

cursor.execute(create_table_query)
conn.commit()

#check if the table was created successfully
the_table = '''SELECT name FROM sqlite_master WHERE type='table' AND name='employee' '''
cursor.execute(the_table)
table_exists = cursor.fetchone()

if table_exists:
    print('Table exists.')
else:
    print('Table does not exist.')

#Insert the data in the table of the database
employee_insertion = [
    ('Johnny Walker', 'Trainee', 1000000),
    ('Vat 69', 'Boss', 50000000)
]

insert_query = "INSERT INTO employee (name, designation, salary) VALUES (?,?,?)"
cursor.executemany(insert_query, employee_insertion)
conn.commit()

#Retrieve all the employee data
select_query = "SELECT * FROM employee"
cursor.execute(select_query)
employee_data = cursor.fetchall()

#Display the data
for employee in employee_data:
    print("ID:", employee[0])
    print("Name:", employee[1])
    print("Designation:", employee[2])
    print("Salary:", employee[3])
    print()

#close the connection
conn.close()

# Wait for user input before closing the window
input("Press Enter to exit...")
