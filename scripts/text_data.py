with open('data.txt','r') as file:
    content = file.read()
    print(content)

with open('data.txt','a') as file:
    file.write("\nHello World")
    file.write("\nОгромные, просто огромные слоны")

with open('data.txt','r') as file:
    for line in file:
        print(line, end='')

with open('data.txt','rb') as source:
    with open('data_copy.txt','wb') as new_file:
        new_file.write(source.read())

