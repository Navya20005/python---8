class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class Intern(Student, Employee):
    def __init__(self, name, course, salary):
        Person.__init__(self, name)
        self.course = course
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Salary:", self.salary)


i = Intern("Navya", "Python Full Stack", 25000)

i.display()

print(Intern.mro())