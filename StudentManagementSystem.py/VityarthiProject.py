import json

students = {}  #Stores student details
attendance = {}  #Stores attendance records

USERNAME = "vitbhopal"
PASSWORD = "vit123"

def login():
    print("-=| Login |=-")
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    if user == USERNAME and pwd == PASSWORD:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials. Try again.\n")
        return False

def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists.\n")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Age": age, "Marks": float(marks)}
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No student records found.\n")
    else:
        print("-=| Student Records |=-")
        for roll, details in students.items():
            print(f"Roll No: {roll}, Name: {details['Name']}, Age: {details['Age']}, Marks: {details['Marks']}")
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        details = students[roll]
        print(f"Found: Name: {details['Name']}, Age: {details['Age']}, Marks: {details['Marks']}\n")
    else:
        print("Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter new Name: ")
        age = input("Enter new Age: ")
        marks = input("Enter new Marks: ")
        students[roll] = {"Name": name, "Age": age, "Marks": float(marks)}
        print("Student updated!\n")
    else:
        print("Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        if roll in attendance:
            del attendance[roll]
        print("Student deleted!\n")
    else:
        print("Student not found.\n")

def mark_attendance():
    roll = input("Enter Roll Number to mark attendance: ")
    if roll not in students:
        print("Student not found.\n")
        return
    status = input("Enter Attendance (P for Present, A for Absent): ").upper()
    if status not in ['P', 'A']:
        print("Invalid attendance status.\n")
        return
    if roll not in attendance:
        attendance[roll] = []
    attendance[roll].append(status)
    print("Attendance marked!\n")

def view_attendance():
    if not attendance:
        print("No attendance records found.\n")
        return
    print("== Attendance Records ==")
    for roll, records in attendance.items():
        total = len(records)
        present = records.count('P')
        print(f"Roll No: {roll}, Present: {present}/{total} days")
    print()

def marks_analysis():
    if not students:
        print("No student records to analyze.\n")
        return
    total_marks = sum(details['Marks'] for details in students.values())
    count = len(students)
    avg_marks = total_marks / count
    print(f"Average Marks: {avg_marks:.2f}\n")
    print("Students Passed (Marks >= 35):")
    for roll, details in students.items():
        if details['Marks'] >= 35:
            print(f"{roll} - {details['Name']} : {details['Marks']}")
    print("\nStudents Failed (Marks < 35):")
    for roll, details in students.items():
        if details['Marks'] < 35:
            print(f"{roll} - {details['Name']} : {details['Marks']}")
    print()

def save_data():
    data = {"students": students, "attendance": attendance}
    with open("student_data.json", "w") as f:
        json.dump(data, f)
    print("Data saved to student_data.json\n")

def load_data():
    global students, attendance
    try:
        with open("student_data.json", "r") as f:
            data = json.load(f)
            students = data.get("students", {})
            for k, v in students.items():
                v['Marks'] = float(v['Marks'])  # Convert marks back to float
            attendance = data.get("attendance", {})
        print("Data loaded from student_data.json\n")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.\n")

if __name__ == "__main__":
    print("-=| Student Management System |=-")
    if not login():
        exit()

    load_data()

    while True:
        print("Options:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Mark Attendance")
        print("7. View Attendance Summary")
        print("8. Marks Analysis")
        print("9. Save Data")
        print("10. Exit")
        choice = input("Enter choice (1-10): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            mark_attendance()
        elif choice == "7":
            view_attendance()
        elif choice == "8":
            marks_analysis()
        elif choice == "9":
            save_data()
        elif choice == "10":
            print("Saving data and exiting. Goodbye!")
            save_data()
            break
        else:
            print("Invalid choice. Try again.\n")
