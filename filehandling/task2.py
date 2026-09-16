# write a program to count the number of lines in a file 

with open ("data.txt" , "r") as file:

     lines= file.readlines()

print("Number of lines =",len(lines))