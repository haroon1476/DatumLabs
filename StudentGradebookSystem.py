import json  # for saving and loading student data

class Student:

    next_id = 1
    all_students = [] # static list to store all the students

    def __init__(self, name):
        self.id = Student.next_id #self-incremental id assigned
        self.name = name
        self.grades = {}  # dictionary to store name along with grades
        Student.next_id += 1

    def addCourse(self, course, grade):
        self.grades[course] = grade

    def calculateGPA(self):
        total_points = 0
        total_courses = len(self.grades)

        for grade in self.grades.values():
            total_points += grade * 3  # Assuming each course has 3 credits for simple calculations purposes

        if total_courses == 0:
            return 0

        total_credits = total_courses * 3
        return round(total_points / total_credits, 2)

    # Function to convert every student object to jason format. WIll be helpful in writing data
    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "grades": self.grades
        }


def addStudent():
    name = input("Enter student name: ")
    student = Student(name)

    while True:
        courseName = input("Enter course name (or enter 'done' to finish the course input): ")
        if courseName.lower() == 'done':
            break
        grade = float(input(f"Enter grade for {courseName} (0 to 4): "))
        student.addCourse(courseName, grade)

    Student.all_students.append(student)
    print(f"Student '{name}' added with ID {student.id}")


def updateStudentGrades():
    student_id = int(input("Enter student ID to update: "))
    student = None

    for s in Student.all_students:
        if s.id == student_id:
            student = s
            break

    if student is None:
        print("Student not found.")
        return

    course = input("Enter course to add or update: ")
    grade = float(input("Enter grade (0 to 4): "))

    # If the course is already present, grades will be updated. If course is not present, grades will be added.
    student.addCourse(course, grade)
    print(" Grade updated.")

def showGPA():
    student_id = int(input("Enter student ID: "))
    for student in Student.all_students:
        if student.id == student_id:
            gpa = student.calculateGPA()
            print(f"GPA of {student.name} (ID {student.id}) is: {gpa}")
            return
    print("Student not found.")

def saveToFile():

    data = []  # to store all the students
    for s in Student.all_students:
        student_dict = s.toDict()  # function call to convert student to list
        data.append(student_dict)   

    # writing the student data inside data list to the jason file
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully.")

def loadFromFile():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
            for student_data in data:
                student = Student(student_data["name"])
                student.id = student_data["id"]
                student.grades = student_data["grades"]
                Student.all_students.append(student)
            if Student.all_students:
                Student.next_id = max(s.id for s in Student.all_students) + 1 #updating id id generator
            print("Students loaded from file.")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")


def main():

    loadFromFile()
    while True:
        print("1. Add Student")
        print("2. Update Grades")
        print("3. Show GPA")
        print("4. Save and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            addStudent()
        elif choice == '2':
            updateStudentGrades()
        elif choice == '3':
            showGPA()
        elif choice == '4':
            saveToFile()
            print("Exited successfully!")
            break
        else:
            print("Invalid choice. Try again.")

# Calling the main function
main()