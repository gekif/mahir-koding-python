list_example_1 = [42, 'Python', 3.85, 50]
list_example_1.insert(1, 'Data Science')
# list_example.append('JavaScript')
# list_example.remove('Python')
# list_example.pop()
# del list_example[2]
list_example_1.clear()
print(list_example_1)

print("\n")
list_example_2 = [40, 51, 20, 71, 80]

for item in list_example_2:
    # print(item)
    if item % 2 == 0:
        print(item)

print("\n")
if 40 in list_example_2:
    print("Terdapat angka 40 pada list example")

print("\n")
length = len(list_example_2)

print("\n")
list_example_3 = list_example_2
list_example_3[0] = 100
print(list_example_3)

print("\n")
list_example_4 = list_example_2.copy()
list_example_4[0] = 100
print(list_example_4)

print("\n")
list_example_5 = [40, 55, 20]
list_example_6 = [70, 100]

list_example_5.extend(list_example_6)
list_example_5.sort()
list_example_5.reverse()
print(list_example_5)