# Input
angka_1 = 10
angka_2 = 5


# Operator

# Addition
hasil_penjumlahan = angka_1 + angka_2

# Modulus
hasil_modulus = angka_1 % angka_2

# Exponention
hasil_exponention = angka_1 ** angka_2


# Operators Implementation



# Output_1
print("=== Numbers Implementation ===")
print(f"Hasil Penjumlahan: {hasil_penjumlahan}")
print(f"Hasil Modulus: {hasil_modulus}")
print(f"Hasil Exponention: {hasil_exponention}")

print("\n")

print("=== Operators Implementation ===")
angka = 5
print(f"Angka Sebelum Ditambah: {angka}")
angka += 10
print(f"Angka Setelah Ditambah: {angka}")

print("\n")
print("=== Division Implementation ===")
angka_3 = 8
angka_4 = 3
hasil_division = angka_3 / angka_4
hasil_floor_division = angka_3 // angka_4
print(f"Hasil Division ({angka_3} / {angka_4}): {round(hasil_division, 2)}")
print(f"Hasil Floor Division ({angka_3} // {angka_4}): {hasil_floor_division}")

# Built In Function Implementation
import math
print("\n")
print("=== Built In Function Implementation ===")
angka_5 = 16
akar_kuadrat = math.sqrt(angka_5)
print(f"Akar Kuadrat dari {angka_5} adalah: {int(akar_kuadrat)}")
