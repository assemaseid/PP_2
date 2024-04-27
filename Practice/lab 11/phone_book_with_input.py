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

while True:
    print("1. Add new contact")
    print("2. Update existing contact")
    print("3. Quare")
    print("4. Delete existing contact")
    print("Enter any other key to exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        cur.execute("INSERT INTO phone_book(first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                    (first_name, last_name, phone_number))

    elif choice == "2":
        contact_id = input("Enter contact ID to update: ")
        update_choice = input("What do you want to update? (1. First Name, 2. Phone Number): ")

        if update_choice == "1":
            new_first_name = input("Enter new first name: ")
            cur.execute("UPDATE phone_book SET first_name = %s WHERE contact_id = %s", (new_first_name, contact_id))
        elif update_choice == "2":
            new_phone_number = input("Enter new phone number: ")
            cur.execute("UPDATE phone_book SET phone_number = %s WHERE contact_id = %s", (new_phone_number, contact_id))
    elif choice == "3":
        cur.execute("SELECT * FROM phone_book")
        rows = cur.fetchall()
        for row in rows:
            print(f"{row[0]} - {row[1]} {row[2]}: {row[3]}")
    elif choice == "4":
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM  phone_book WHERE first_name = %s OR last_name = %s", (name, name))
        
    else:
        break

    

    conn.commit()  # Commit after each update or insert

cur.close()
conn.close()
