# write a program write 5 user - entered sentance to a file 

with open("data.txt", "w") as file:

    for i in range(5):
        sentance= input("Enter the sentance: ")
        file.write(sentance + "\n")


print("5 sentance written to the file")