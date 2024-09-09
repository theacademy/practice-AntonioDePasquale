import mysql.connector
# pip install mysql-connector-python

# sql code for creating your db
'''
create database contactList2;
use contactList2;

create table contacts(
	id int primary key auto_increment,
    fullName varchar(255),
    phone varchar(15),
    email varchar(100)
);
'''

# Database Config
db_config = {
    'user': 'root',
    'password': 'Ascalon357673!',
    'host': 'localhost', #127.0.0.1
    'database': 'contactList2'

}

class Contact:
    def __init__(self, id, fullName, phone, email):
        self.contact_id = id
        self.fullName = fullName
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.fullName}, Phone: {self.phone}, Email: {self.email}"

class ContactList:
    def __init__(self):
        self.conn = mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor(dictionary = True)
        #
        self.contacts = []


    def create_contact(self, fullName, phone, email):
        sql = "INSERT INTO contacts (fullName, phone, email) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (fullName, phone, email))
        self.conn.commit()
        newContact = Contact(self.cursor.lastrowid, fullName, phone, email)
        self.contacts.append(newContact) # type: ignore
        print(f"Contact added successfully: {newContact}")


    def read_contacts(self):
        sql = "SELECT * FROM contacts"
        self.cursor.execute(sql)
        self.contacts = self.cursor.fetchall()
        print("\nContacts:")
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def update_contact(self, contact_id, new_fullName=None, new_phone=None, new_email=None):
        sql = "SELECT * FROM contacts WHERE id = %s"
        self.cursor.execute(sql, (contact_id,))
        contact = self.cursor.fetchone()
        if not contact:
            print(f"Contact with ID {contact_id} not found.")
            return
        
        updates = []
        params = []

        if new_fullName:
            updates.append("fullName = %s")
            params.append(new_fullName)
        if new_phone:
            updates.append("phone = %s")
            params.append(new_phone)
        if new_email:
            updates.append("email = %s")
            params.append(new_email)

        if updates:
            sql = f"UPDATE contacts SET {', '.join(updates)} WHERE id = %s"
            params.append(contact_id)
            self.cursor.execute(sql, params)
            self.conn.commit()
            print(f"Contact ID {contact_id} updated successfully.")
        else:
            print("No updates provided.")

    def delete_contact(self, contact_id):
        sql = "SELECT * FROM contacts WHERE id = %s"
        self.cursor.execute(sql, (contact_id,))
        contact = self.cursor.fetchone()
        if not contact:
            print(f"Contact with ID {contact_id} not found.")
            return

        # Delete the contact
        sql = "DELETE FROM contacts WHERE id = %s"
        self.cursor.execute(sql, (contact_id,))
        self.conn.commit()
        print(f"Contact ID {contact_id} deleted successfully.")

    def __del__(self):
        self.cursor.close()
        self.conn.close()
  

def main():
    contact_list = ContactList()

    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            fullName = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_list.create_contact(fullName, phone, email)
        elif choice == '2':
            contact_list.read_contacts()
        elif choice == '3':
            contact_id = input("Enter the contact id of the contact to update: ")
            new_fullName = input("Enter new full name (leave blank to keep current): ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            contact_list.update_contact(contact_id, new_fullName if new_fullName else None, new_phone if new_phone else None, new_email if new_email else None)
        elif choice == '4':
            contact_id = input("Enter the contact ID of the contact to delete: ")
            contact_list.delete_contact(contact_id)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
