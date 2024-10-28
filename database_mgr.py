import sqlite3

def create_database():
    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL
        )
    """)
    print("Database and users table created.")
    conn.commit()
    conn.close()

def add_user(name, email, role):
    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (name, email, role) VALUES (?, ?, ?)", (name, email, role))
        print(f"User {name} added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: A user with the email {email} already exists.")
    
    conn.commit()
    conn.close()

def get_users(role=None):
    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()
    
    if role:
        cursor.execute("SELECT * FROM users WHERE role = ?", (role,))
    else:
        cursor.execute("SELECT * FROM users")
        
    users = cursor.fetchall()
    for user in users:
        print(user)
    
    conn.close()

def main():
    while True:
        print("\nDatabase Management Tool")
        print("1. Create Database and Table")
        print("2. Add User")
        print("3. View All Users")
        print("4. View Users by Role")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_database()
        elif choice == "2":
            name = input("Enter name: ")
            email = input("Enter email: ")
            role = input("Enter role: ")
            add_user(name, email, role)
        elif choice == "3":
            get_users()
        elif choice == "4":
            role = input("Enter role to filter by: ")
            get_users(role)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
