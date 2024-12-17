def number_students():
    return int(input("Enter the number of students: "))

def students_info(number_students):
    students = []
    for i in range(0,number_students,1):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Date of Birth (DoB): ")
        students.append({"id": student_id, "name": student_name, "dob": student_dob})
    return students

def number_courses():
    return int(input("Enter the number of courses: "))

def courses_info(number_courses):
    courses = []
    for _ in range(number_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append({"id": course_id, "name": course_name})
    return courses

def marks(students, course):
    print(f"Entering marks for course: {course['name']}")
    course_marks = {}
    for student in students:
        mark = float(input(f"Enter marks for student {student['name']} (ID: {student['id']}): "))
        course_marks[student["id"]] = mark
    return {course["id"]: course_marks}

def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")
    print()

def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")
    print()

def show_student_marks(marks):
    print("Student Marks:")
    for student_id, mark_info in marks.items():
        print(f"Student ID: {student_id}, Course: {mark_info['course']}, Mark: {mark_info['mark']}")
    print()

def main():
    num_students = number_students()
    students = students_info(num_students)

    num_courses = number_courses()
    courses = courses_info(num_courses)

    marks_data = {}
    while True:
        print("\nMenu:")
        print("1. List all courses")
        print("2. List all students")
        print("3. Input marks for a course")
        print("4. Show student marks")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            list_courses(courses)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            list_courses(courses)
            course_id = input("Select course by ID: ")
            selected_course = next((course for course in courses if course["id"] == course_id), None)
            if selected_course:
                course_marks = marks(students, selected_course)
                marks_data.update(course_marks)
            else:
                print("Invalid course ID.")
        elif choice == "4":
            show_student_marks(marks_data, courses)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
