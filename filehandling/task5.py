# write a program to append a list of string to an existing file 

strings = ["Hello", "Python is easy", "I am learning Python"]

with open("data.txt" , "a") as file:
    for string in strings:
        file.write(string + "\n")

print("string appended successfully")