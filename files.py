with open("coding-studio.txt", "w") as file:
    file.write("Hello Coding Studio!\n")
    file.write("This is a new line.\n")

with open("coding-studio.txt", "a") as file:
    file.write("Appending a new line.\n")

with open("coding-studio.txt", "r") as file:
    content = file.read()
    print(content)