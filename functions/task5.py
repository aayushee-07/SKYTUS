# check if fun is palindrome 

def palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False 

word=input("Enter a word: ")

if palindrome(word):
    print("Palindrome")

else:
   print("Not palindrome")