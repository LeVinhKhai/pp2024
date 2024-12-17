class Person:
    def __init__(self, id, name, dob=None):
        self.id = id
        self.name = name
        self.dob = dob

    def __str__(self):
        dob_info = f", DOB: {self.dob}" if self.dob else ""
        return f"ID: {self.id}, Name: {self.name}{dob_info}"


class Student(Person):
    pass


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Course ID: {self.id}, Name: {self.name}"


class Marks:
    def __init__(self):
        self.marks_data = {}

    def add_marks(self, students, course):
        print(f"Enter marks for students in the course '{course.name}':")
        for student in students:
            try:
                score = float(input(f"Enter marks for {student.name} (ID: {student.id}): "))
                if course.id not in self.marks_data:
                    self.marks_data[course.id] = {}
                self.marks_data[course.id][student.id] = score
            except ValueError:
                print("Invalid marks input. Skipping this student.")

    def display_marks(self, students, course):
        print(f"\nMarks for course '{course.name}':")
        if course.id in self.marks_data:
            for student in students:
                score = self.marks_data[course.id].get(student.id, "No marks recorded")
                print(f"{student.name} (ID: {student.id}): {score}")
        else:
            print("No marks have been entered for this course yet.")


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Marks()

    def add_students(self):
        try:
            total_students = int(input("How many students do you want to add? "))
            for _ in range(total_students):
                id = input("Enter student ID: ")
                name = input("Enter student name: ")
                dob = input("Enter student date of birth (optional): ")
                self.students.append(Student(id, name, dob))
        except ValueError:
            print("Invalid input. Please try again.")

    def add_courses(self):
        try:
            total_courses = int(input("How many courses do you want to add? "))
            for _ in range(total_courses):
                id = input("Enter course ID: ")
                name = input("Enter course name: ")
                self.courses.append(Course(id, name))
        except ValueError:
            print("Invalid input. Please try again.")

    def show_students(self):
        print("\n--- List of Students ---")
        if self.students:
            for student in self.students:
                print(student)
        else:
            print("No students have been added yet.")

    def show_courses(self):
        print("\n--- List of Courses ---")
        if self.courses:
            for course in self.courses:
                print(course)
        else:
            print("No courses have been added yet.")

    def enter_marks(self):
        self.show_courses()
        course_id = input("Enter the course ID to enter marks for: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if course:
            self.marks.add_marks(self.students, course)
        else:
            print("Invalid course ID.")

    def view_marks(self):
        self.show_courses()
        course_id = input("Enter the course ID to view marks: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if course:
            self.marks.display_marks(self.students, course)
        else:
            print("Invalid course ID.")

    def start(self):
        while True:
            print("\n--- University System Menu ---")
            print("1. Add Students")
            print("2. Add Courses")
            print("3. List Students")
            print("4. List Courses")
            print("5. Input Marks")
            print("6. View Marks")
            print("0. Exit")
            try:
                choice = int(input("Select an option: "))
                if choice == 1:
                    self.add_students()
                elif choice == 2:
                    self.add_courses()
                elif choice == 3:
                    self.show_students()
                elif choice == 4:
                    self.show_courses()
                elif choice == 5:
                    self.enter_marks()
                elif choice == 6:
                    self.view_marks()
                elif choice == 0:
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid option. Please select again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    system = SchoolSystem()
    system.start()
