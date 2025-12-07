import streamlit as st
import json
import os

FILE = "students.json"

# Load students
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save students
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

students = load_data()

st.title("📚 Student Management System (Streamlit Web App)")

menu = ["Add Student", "View Students", "Search Student", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

# Add Student
if choice == "Add Student":
    st.header("➕ Add Student")
    id = st.text_input("Student ID")
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, max_value=120)
    course = st.text_input("Course")
    marks = st.number_input("Marks", min_value=0, max_value=100)

    if st.button("Add"):
        students.append({"id": id, "name": name, "age": age, "course": course, "marks": marks})
        save_data(students)
        st.success("Student added successfully!")

# View Students
elif choice == "View Students":
    st.header("📄 View All Students")
    if students:
        st.table(students)
    else:
        st.info("No student records found.")

# Search Student
elif choice == "Search Student":
    st.header("🔍 Search Student by Name")
    search_name = st.text_input("Enter name to search")

    if st.button("Search"):
        results = [s for s in students if s["name"].lower() == search_name.lower()]

        if results:
            st.table(results)
        else:
            st.error("Student not found.")

# Update Student
elif choice == "Update Student":
    st.header("✏️ Update Student Details")
    update_id = st.text_input("Enter Student ID to Update")

    # Find student
    student = next((s for s in students if s["id"] == update_id), None)

    if student:
        name = st.text_input("New Name", student["name"])
        age = st.number_input("New Age", min_value=1, max_value=120, value=student["age"])
        course = st.text_input("New Course", student["course"])
        marks = st.number_input("New Marks", min_value=0, max_value=100, value=student["marks"])

        if st.button("Update"):
            student["name"] = name
            student["age"] = age
            student["course"] = course
            student["marks"] = marks
            save_data(students)
            st.success("Student details updated successfully!")
    else:
        if update_id:
            st.error("Invalid Student ID.")

# Delete Student
elif choice == "Delete Student":
    st.header("🗑 Delete Student")
    delete_id = st.text_input("Enter Student ID to Delete")

    if st.button("Delete"):
        new_students = [s for s in students if s["id"] != delete_id]

        if len(new_students) != len(students):
            students = new_students
            save_data(students)
            st.success("Student deleted successfully!")
        else:
            st.error("Invalid Student ID.")
