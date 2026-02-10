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

print("\n")
tuple_example = (42, 'Python', 3.85, 50)
print(tuple_example)
print(tuple_example[1])
print(tuple_example[-2])

print("\n")
customer = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
print(customer)
print(customer['name'])

print("\n")
numbers1 = {1, 2, 3, 4, 5}
numbers2 = {4, 5, 6, 7, 8}
union_set = numbers1.union(numbers2)
intersection_set = numbers1.intersection(numbers2)
difference = numbers1.difference(numbers2)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference)