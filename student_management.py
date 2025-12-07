students = []

print("===== Student Management System =====")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Save & Exit")

while True:
    choice = input("Enter your choice: ")

    if choice not in ['1','2','3','4','5','6']:
        print("Invalid choice. Please try again.")
        break

    elif choice == '1':
        row = []
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        course = input("Enter Student Course: ")
        marks = input("Enter Student Marks: ")

        row.append(id)
        row.append(name)
        row.append(age)
        row.append(course)
        row.append(marks)
        students.append(row)

        print("Student added successfully!")

    elif choice == '2':
        print("ID\tName\tAge\tCourse\tMarks")
        for student in students:
            print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")

    elif choice == '3':
        search_name = input("Enter the name of the student to search: ")
        found = False
        print("ID\tName\tAge\tCourse\tMarks")
        for student in students:
            if student[1] == search_name:
                print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}")
                found = True
        if not found:
            print("Student not found.")

    elif choice == '4':
        update_det = input("Enter the column to update (name/age/course/marks): ")
        update_id = input("Enter Student ID: ")
        found = False

        for student in students:
            if student[0] == update_id:
                found = True
                if update_det.lower() == 'name':
                    student[1] = input("Enter new name: ")
                elif update_det.lower() == 'age':
                    student[2] = input("Enter new age: ")
                elif update_det.lower() == 'course':
                    student[3] = input("Enter new course: ")
                elif update_det.lower() == 'marks':
                    student[4] = input("Enter new marks: ")
                else:
                    print("Invalid field!")
                    break
                print("Student details updated successfully!")
                break

        if not found:
            print("Invalid Student ID.")

    elif choice == '5':
        delete_id = input("Enter Student ID to delete: ")
        found = False
        for student in students:
            if student[0] == delete_id:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break
        if not found:
            print("Invalid Student ID.")

    elif choice == '6':
        print("Saving data and exiting...")
        break
