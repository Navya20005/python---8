class Father:
    def show(self):
        print("Father")


class Mother:
    def show(self):
        print("Mother")


class Child(Father, Mother):
    pass


c = Child()

c.show()

print(Child.mro())