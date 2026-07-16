import csv
import os

FILE_NAME = "students.csv"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No", "Name", "Maths", "Physics", "Python", "Total", "Percentage", "Grade"])


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    maths = int(input("Maths Marks: "))
    physics = int(input("Physics Marks: "))
    python = int(input("Python Marks: "))

    total = maths + physics + python
    percentage = total / 3
    grade = calculate_grade(percentage)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, maths, physics, python, total, f"{percentage:.2f}", grade])

    print("Student added successfully!")


def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_student():
    roll = input("Enter Roll Number to search: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == roll:
                print("\nStudent Found")
                print("----------------------------")
                print("Roll No :", row[0])
                print("Name :", row[1])
                print("Maths :", row[2])
                print("Physics :", row[3])
                print("Python :", row[4])
                print("Total :", row[5])
                print("Percentage :", row[6])
                print("Grade :", row[7])
                found = True
                break

    if not found:
        print("Student not found.")


while True:
    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
