# write a program to read a file and print only lines that contain specific word 

word = input("Enter the word to search: ")

with open("data.txt", "r") as file:
    for line in file:
        if word in line:
            print(line)