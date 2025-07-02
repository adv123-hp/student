import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    dob TEXT,
    course TEXT,
    year INTEGER,
    email TEXT,
    phone TEXT
)
''')
conn.commit()

# Menu display
def menu():
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Name")
    print("5. Delete Student")
    print("6. Exit")

# Function to add student
def add_student():
    sid = int(input("Student ID: "))
    name = input("Name: ")
    gender = input("Gender: ")
    dob = input("DOB (YYYY-MM-DD): ")
    course = input("Course: ")
    year = int(input("Year: "))
    email = input("Email: ")
    phone = input("Phone: ")
    cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                   (sid, name, gender, dob, course, year, email, phone))
    conn.commit()
    print("Student added.")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to search student
def search_student():
    sid = int(input("Enter Student ID: "))
    cursor.execute("SELECT * FROM student WHERE student_id=?", (sid,))
    result = cursor.fetchone()
    print(result if result else "Not found.")

# Function to update name
def update_student():
    sid = int(input("Enter Student ID to update: "))
    new_name = input("Enter new name: ")
    cursor.execute("UPDATE student SET name=? WHERE student_id=?", (new_name, sid))
    conn.commit()
    print("Student updated.")

# Function to delete student
def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    cursor.execute("DELETE FROM student WHERE student_id=?", (sid,))
    conn.commit()
    print("Student deleted.")

# Main loop
while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice!")

conn.close()
