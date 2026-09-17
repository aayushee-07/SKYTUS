# write a program to open a file and handle the "file not found" error

try:
    with open ("file.txt" , "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found! Please try again")