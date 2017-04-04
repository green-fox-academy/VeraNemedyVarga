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
        print("Hire brilliant junioor software developers.")

class LagopusClass(object):
    

neni = Person()
neni.introduce()
neni.get_goal()

student = Student()
student.get_goal()
student.introduce()
print(student.skip_days(4))

mentor = Mentor()
mentor.introduce()

sponsor = Sponsor()
sponsor.introduce()
print(sponsor.hire())
sponsor.get_goal()
