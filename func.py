def greet():
    print("Hello stranger")
    print("Nice to meet you")

greet()
greet()

print("\n")

def greet_with_argument(name, age):
    print(f"Hello {name}")
    print(f"You are {age} years old")

greet_with_argument(name="Fikar", age=38)

print("\n")

def add5(number):
    total = number + 5
    return total

print(add5(10))

print("\n")
number = 10
number_added_5 = add5(number)
print(number_added_5)

print("\n")
number = 20
total = lambda num: num + 5
print(total(number))
