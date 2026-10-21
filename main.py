<<<<<<< HEAD

import json
import os

FILE_NAME = "students.json"


def load_students():
    """Load student records from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read student data.")
        return []


def save_students(students):
    """Save student records to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def find_student(students, student_id):
    """Find a student using their ID."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(students, student_id):
        print("This student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course name: ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        age = int(input("Enter student age: "))
        if age <= 0:
            print("Age must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()
    student = find_student(students, student_id)

    if student:
        print("\nStudent found:")
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
    else:
        print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")

    name = input(f"Name [{student['name']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    age_text = input(f"Age [{student['age']}]: ").strip()

    if name:
        student["name"] = name

    if course:
        student["course"] = course

    if age_text:
        try:
            age = int(age_text)
            if age <= 0:
                print("Age must be greater than zero.")
                return
            student["age"] = age
        except ValueError:
            print("Invalid age. Update cancelled.")
            return

    save_students(students)
    print("Student updated successfully!")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    confirm = input(
        f"Delete {student['name']}? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("7. Count Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "7":
            print("Total students:", len(students))
        elif choice == "6":
            print("Thank you for using the application!")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
=======

import json
import os

FILE_NAME = "students.json"


def load_students():
    """Load student records from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read student data.")
        return []


def save_students(students):
    """Save student records to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def find_student(students, student_id):
    """Find a student using their ID."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student(students):
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(students, student_id):
        print("This student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course name: ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        age = int(input("Enter student age: "))
        if age <= 0:
            print("Age must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()
    student = find_student(students, student_id)

    if student:
        print("\nStudent found:")
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
    else:
        print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")

    name = input(f"Name [{student['name']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    age_text = input(f"Age [{student['age']}]: ").strip()

    if name:
        student["name"] = name

    if course:
        student["course"] = course

    if age_text:
        try:
            age = int(age_text)
            if age <= 0:
                print("Age must be greater than zero.")
                return
            student["age"] = age
        except ValueError:
            print("Invalid age. Update cancelled.")
            return

    save_students(students)
    print("Student updated successfully!")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    confirm = input(
        f"Delete {student['name']}? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    students = load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using the application!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
>>>>>>> 8d898ec14d20bf94680a8fdb992a13cdca343694
