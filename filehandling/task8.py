# write a program to merge the content of two text file into the third 

with open ("data.txt", "r") as file1:
    content1= file1.read()

with open ("data2.txt","r") as file2:
    content2= file2.read()

with open ("marge.txt", "w")as file3:
    file3.write(content1)
    file3.write("\n")
    file3.write(content2)

print("Files marged successfully")