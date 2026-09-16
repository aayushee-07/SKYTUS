# write a program to read a csv file and display its content in formatted way 

import csv 

with open ("data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(" | ".join(row))