with open('input.txt', 'w+') as file:
    file.write("Computer Science")
    file.seek(0)
    print(file.read(3))
