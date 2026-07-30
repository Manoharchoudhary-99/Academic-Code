class Student:

    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def show_details(self):
        print("Student Details")
        print("Roll Number :", self.roll_no)
        print("Name        :", self.name)
        print("Course      :", self.course)


# Creating an object
student1 = Student(30, "MAnohar", "Computer Science")

# Calling the method
student1.show_details()