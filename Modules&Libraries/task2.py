# create a module to perform string operations 

import string_operations

text = input("Enter a string: ")

print("Reverse:", string_operations.reverse_string(text))
print("Number of vowels:", string_operations.count_vowels(text))