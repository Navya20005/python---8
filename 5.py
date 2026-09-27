class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course, marks):
        super().__init__(name, age)
        self.course = course
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)


s = Student("Navya", 21, "Python Full Stack", 85)

s.display()