class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Puppy(Dog):
    def play(self):
        print("Puppy is playing")


p = Puppy()

p.eat()
p.bark()
p.play()