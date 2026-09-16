# fun to count vowels in a string 

def count_vowels(text):
    count=0

    for char in text:
        if char in "aeiou":
           count=count+1

    return count         


text = input("Enter a string:")

print("number of vowels=",count_vowels(text))
