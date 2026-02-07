x = 5
y = 10
z = 15

print(x > y)
print(x < y)

print(not(x > y))

print(x < y and y > z)
print(x < y and y > z)

if x == y:
    print("X sama dengan Y")

if x < y:
    print("X kurang dari Y")


if x > y:
    print("X lebih besar dari Y")
else:
    print("X kurang dari Y")


if x > y and z < y:
    print("X lebih besar dari Y")
else:
    print("X kurang dari Y")


if x > y:
    print("X lebih besar dari Y")
elif x < y:
    print("X kurang dari Y")
elif z > y:
    print("Z lebih besar dari Y")
else:
    print("Kondisi diatas semuanya salah")