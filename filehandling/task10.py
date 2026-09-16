# write a program to backup a file by copying its content to another file 

with open ("data.txt", "r")as file:
    content= file.read()

with open ("backup.txt", "w") as backup:
    backup.write(content)

print("Backup created sucessfully")