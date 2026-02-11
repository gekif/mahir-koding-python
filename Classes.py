class Angka:
    jumlah = 5

a = Angka()
print(a.jumlah)

b = Angka()
print(b.jumlah)

class Person:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def greet(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and my score is {self.score}.")

person1 = Person("Alice", 30, 85)
person2 = Person("Bob", 25, 90)
print("\n")
print(person1.name)
print(person1.age)
print(person1.score)
person1.greet()
person2.greet()

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")

class Cat(Animal):
    def __init__(self, name, age, color, weight):
        super().__init__(name, age)
        self.color = color
        self.weight = weight

    def meow(self):
        print(f"{self.name} says Meow!")

class Dog(Animal):
    def __init__(self, name, age, types):
        super().__init__(name, age)
        self.types = types

    def bark(self):
        print(f"{self.name} says Woof!")