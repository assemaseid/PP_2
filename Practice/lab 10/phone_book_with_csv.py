import psycopg2
import csv

# Connect to the PostgreSQL database
conn = psycopg2.connect(database="phonebook",
                        user="postgres", 
                        password="72zv5u3xp",
                        host="localhost",
                        port="5432")
                        
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS contacts (
            contact_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone_number VARCHAR(30) NOT NULL
            )""" 
)

# Read data from CSV and insert into the database
try:
    with open("/Users/assemseidkarim/Desktop/PP_2/Practice/lab 10/data.csv", "r") as file:
        content = csv.reader(file, delimiter=";")
        next(content)  # Skip header row
        data = [(row[0], row[1], row[2]) for row in content if len(row) >= 3]
except FileNotFoundError:
    print("The file 'data.csv' was not found.")
except Exception as e:
    print("An error occurred while reading the CSV file:", e)

csv_file = """INSERT INTO contacts (first_name, last_name, phone_number) 
         VALUES (%s, %s, %s)"""

for row in data:
    cur.execute(csv_file, row)

# Prompt user for adding or updating contacts
while True:
    print("1. Add new contact")
    print("2. Update existing contact")
    print("3. Quare")
    print("4. Delete existing contact")
    print("Enter any other key to exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        phone_number = input("Enter phone number: ").strip()
        cur.execute("INSERT INTO contacts(first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                    (first_name, last_name, phone_number))
    elif choice == "2":
        contact_id = input("Enter contact ID to update: ").strip()
        update_choice = input("What do you want to update? (1. First Name, 2. Phone Number): ").strip()
        new_value = input("Enter new value: ").strip()
        
        if update_choice == "1":
            cur.execute("UPDATE contacts SET first_name = %s WHERE contact_id = %s", (new_value, contact_id))
        elif update_choice == "2":
            cur.execute("UPDATE contacts SET phone_number = %s WHERE contact_id = %s", (new_value, contact_id))
    elif choice == "3":
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()
        for row in rows:
            print(f"{row[0]} - {row[1]} {row[2]}: {row[3]}")
    elif choice == "4":
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM  contacts WHERE first_name = %s OR last_name = %s", (name, name))
    else:
        break

# Commit changes and close cursor and connection
conn.commit()
cur.close()
conn.close()
