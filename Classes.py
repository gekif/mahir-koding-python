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

person1 = Person("Alice", 30, 85)
print("\n")
print(person1.name)
print(person1.age)
print(person1.score)