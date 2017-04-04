class Person(object):
    def __init__(self, name='Jane Doe', age=30, gender='female'):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hi, I'm " + self.name + " a " + str(self.age) + " year old " + self.gender)

    def get_goal(self):
        print("My goal is: live for the moment!")

class Student(Person):
    def __init__(self, name="Jane Doe", age=30, gender="female", prev_org="School of Life", skipped_days=0):
        super().__init__(name, age, gender)
        self.prev_org = prev_org
        self.skipped_days = skipped_days

    def get_goal(self):
        print("Be a junior software developer")

    def introduce(self):
        print("Hi, I'm " + self.name + " a " + str(self.age) + " year old " + self.gender + " from " + self.prev_org + " who skipped " + str(self.skipped_days) + " from the course already.")

    def skip_days(self, number_of_days):
        self.number_of_days = number_of_days
        self.skipped_days += self.number_of_days
        return self.skipped_days


class Mentor(Person):
    def __init__(self, name='Jane Doe', age=30, gender='female', level= "Intermediate"):
        super().__init__(name, age, gender)
        self.level = level

    def introduce(self):
        print("Hi, I'm " + self.name + " a " + str(self.age) + " year old " + self.gender + " " + self.level + " mentor.")

class Sponsor(Person):
    def __init__(self, name='Jane Doe', age=30, gender='female', company="Google", hired_students = 0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students

    def introduce(self):
        print("Hi, I'm " + self.name + " a " + str(self.age) + " year old " + self.gender + " who represents " + self.company + " and hired " + str(self.hired_students) + " students so far.")

    def hire(self):
        self.hired_students += 1
        return self.hired_students

    def get_goal(self):
        print("Hire brilliant junior software developers.")

class LagopusClass(object):
    def __init__(self, class_name='Lagopus'):
        self.class_name = class_name
        self.students = []
        self.mentors = []

    def add_student(self, Student):
        self.students.append(Student)
        return self.students

    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)

    def info(self):
        print(self.class_name + " class has " + str(len(self.students)) + " students and " + str(len(self.mentors)) + " mentors.")
