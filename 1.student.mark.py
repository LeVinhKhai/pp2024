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


