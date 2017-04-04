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


neni = Person()
neni.introduce()
neni.get_goal()
student = Student()
student.get_goal()
student.introduce()
