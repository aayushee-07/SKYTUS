# check if a word present in a setance 
# in = checks whether something exists inside another thing.

sentance= input("Enter the sentance:")
word= input("Enter the word to search:")

if(word in sentance):
    print("Word is present in the sentence")

else:
     print("Word is not present in the sentence")