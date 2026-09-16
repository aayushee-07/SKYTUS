# write a program to count how many times each word appears in a file

with open("data.txt","r") as file:
    content= file.read()

words= content.split()

count={}

for word in words:
    if word in count:
        count[word]= count[word] +1 

    else:
        count[word]=1

print(count)