import psycopg2

conn = psycopg2.connect(database="phonebook",
                        user="postgres",
                        password="72zv5u3xp",
                        host="localhost",
                        port="5432")

cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS phone_book (
            contact_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone_number VARCHAR(30) NOT NULL
            )"""
            )

# lab 11
# Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
def return_reconds():
    cur.execute("SELECT first_name,last_name,phone_number FROM phone_book")
    for row in cur.fetchall():
        print(row)


# Create procedure to insert new user by name and phone, UPDATE phone if user already exists

def insert_update_new_user():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    cur.execute("SELECT * FROM phone_book WHERE first_name = %s",(firstName,))
    name = cur.fetchone()
    cur.execute("SELECT * FROM phone_book WHERE first_name = %s",(lastName,))
    surname = cur.fetchone()
    if name is None and surname is None:
        phoneNumber = input("Enter phone number: ")
        cur.execute("INSERT INTO phone_book(first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                    (firstName, lastName, phoneNumber))
    else:
        print("This user is already exists. Let's UPDATE your phone number, if you would like?")
        print("1. Yes, 2. No")
        updateChoice = input("Enter your choice: ")
        if updateChoice == "1":
            new_phone_number = input("Enter phone number: ")
            cur.execute("UPDATE phone_book SET phone_number = %s WHERE first_name = %s and last_name = %s", (new_phone_number,firstName,lastName))
        elif updateChoice == "2":
            cur.execute("UPDATE phone_book SET phone_number = %s WHERE first_name = %s ", (" "," "))
            
      
        
# Create procedure to insert many new users by list of name and phone. 
# Use loop and if statement in stored procedure. 
# Check correctness of phone in procedure and return all incorrect data.

def insert_multiple_users():
    incorrect_data = []
    user_list = [("Aruzhan", "Zhaksylykova", "1234"), ("Bauyrzhan","Apekov","5678"), ("Erasyl", "Abdikarim", "9000"),("Hey", "Heloo", "42352")]

    for user in user_list:
        first_name, last_name, phone_number = user
        cur.execute("SELECT first_name, last_name, phone_number FROM phone_book WHERE first_name = %s AND last_name = %s AND phone_number = %s", (first_name, last_name, phone_number))
        matching_rows = cur.fetchall()
        if not matching_rows: 
            if not phone_number.isdigit():
                incorrect_data.append(user)
            else:
                cur.execute("INSERT INTO phone_book (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))

    return incorrect_data


# Create function for querying data FROM the tables with pagination (by limit and offset)
def query_with_pagination(limit,offset):
    cur.execute("SELECT * FROM phone_book limit %s offset %s", (limit, offset))
    for row in cur.fetchall():
        print(row)

# Implement procedure to deleting data FROM tables by username or phone
def delete():
    print("Enter 1. name or 2. phone number to delete:")
    delete_choice = input("Enter your coice to delete: ")
    if delete_choice == "1":
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM  phone_book WHERE first_name = %s OR last_name = %s", (name, name)) 
    elif delete_choice == "2":
        phone = input("Enter phone number to delete: ")
        cur.execute("DELETE FROM  phone_book WHERE phone_number = %s OR last_name = %s", (phone, name)) 

while True:
    print("1. Add new contact")
    print("2. UPDATE existing contact")
    print("3. Quare")
    print("4. Delete existing contact")
    print("5. Return all records based on a pattern(part of name, surname, phone number)")
    print("Enter any other key to exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("1. Insert one contact, 2. Insert many contacts")
        insert_choice = input("Enter your insert choice: ")
        if insert_choice == "1":
            insert_update_new_user()
        elif insert_choice == "2":
            insert_multiple_users()
    elif choice == "2":
        contact_id = input("Enter contact ID to UPDATE: ")
        update_choice = input("What do you want to UPDATE? (1. First Name, 2. Phone Number): ")

        if update_choice == "1":
            new_first_name = input("Enter new first name: ")
            cur.execute("UPDATE phone_book SET first_name = %s WHERE contact_id = %s", (new_first_name, contact_id))
        elif update_choice == "2":
            new_phone_number = input("Enter new phone number: ")
            cur.execute("UPDATE phone_book SET phone_number = %s WHERE contact_id = %s", (new_phone_number, contact_id))
    elif choice == "3":
        query_with_pagination(3,2)
    elif choice == "4":
        delete()
    elif choice == "5":
        return_reconds()  
    else:
        break
    conn.commit() 



cur.close()
conn.close()
