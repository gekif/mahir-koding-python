for i in range(0, 5, 1):
    print(i)

print("\n")
for i in range(0, 8, 1):
    print(i)

print("\n")
for i in range(0, 10, 2):
    print(i)

print("\n")
for i in range(5, 30, 5):
    print(i)

print("\n")
for i in range(6):
    print(f"{i}-Looping")

print("\n")
# Angka kelipatan 3, stop 21
for i in range(3, 50, 3):
    if i == 21:
        break
    print(i)

print("\n")
# Cetak angka ganjil 1 s.d 10
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print("\n")
# Cetak angka genap 1 s.d 10
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)


print("\n")
uang = 100

while uang > 0:
    print(f"Masih punya uang: {uang}")
    uang -= 10

print("Uang sudah habis")
