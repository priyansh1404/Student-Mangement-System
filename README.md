# Student Management System

# Overview of the project
This project is a simple Python-based Student Management System for securely managing student records. It provides basic functions to add, display, search, update, and delete student details, mark and view attendance, and analyze marks. Data is saved and loaded using JSON files, offering persistence across sessions. The system aims to replace manual record-keeping with an efficient, user-friendly digital solution, making it a useful educational tool for learning practical Python programming with data handling and user interaction.

# Features
The features of student management system project include:
•	User login for secure access with a predefined username and password.
•	Adding student details including roll number, name, age, and marks.
•	Displaying all student records in a readable format.
•	Searching for a student by roll number to view their details.
•	Updating student details such as name, age, and marks.
•	Deleting student records along with their attendance.
•	Marking attendance for students with status as Present or Absent.
•	Viewing attendance summaries showing present days against total days for each student.
•	Analyzing marks with average calculation and lists of students who passed or failed.
•	Saving and loading student and attendance data as JSON files for persistence.
These features cover basic CRUD (Create, Read, Update, Delete) operations essential to student data management, attendance tracking, and performance analysis in an educational setting.

# Technologies/tools used
•	Python language
•	VS code
•	Modules

# Steps to install & run the project
•	Install Python 
•	SetUp VS code 
•	Create File name StudentManagementSystem.py
•	Write Code and Save it 
•	Execute the Code and record the output

# Instructions for testing
1.	Save the code as a Python file, for example StudentManagementSystem.py
2.	Run the program on your command line or terminal
3.	Login using the credentials hardcoded in the code:
•	Username: vitbhopal
•	Password: pass123
4.	After successful login, test each menu option by entering the corresponding number:
•	Add Student: Enter unique roll number, name, age, and marks. Try adding multiple students.
•	Display Students: Verify all added students are displayed correctly.
•	Search Student: Search for existing roll numbers and non-existent ones to test both cases.
•	Update Student: Update details for a student and confirm changes are shown via display or search.
•	Delete Student: Delete a student and confirm removal from display and attendance.
•	Mark Attendance: Mark attendance (P/A) for students, try some invalid inputs as well.
•	View Attendance Summary: Confirm correct attendance counts and ratios.
•	Marks Analysis: Check average marks, lists of passed (>= 35) and failed (< 35) students.
•	Save Data: Save current data and confirm no errors.
•	Exit: Choose exit and confirm program exits after saving data.
5.	Restart the program and verify that previously saved data loads correctly by choosing options 2 (Display) and 7 (View Attendance).
6.	Try invalid inputs like:
•	Wrong login credentials.
•	Non-numeric or invalid marks.
•	Invalid choice outside 1-10.
•	Entering attendance status other than P or A.
7.	Observe correct error or validation messages and smooth program behavior.
Following these steps will comprehensively test the functionality, data persistence, error handling, and user interaction of your student management system.







