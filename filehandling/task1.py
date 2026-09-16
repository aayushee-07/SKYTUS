# write a program read a file and display it's content 

file = open ("data.txt", "r")

content = file.read()

print(content)

file.close()