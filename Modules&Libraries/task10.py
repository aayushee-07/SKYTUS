    # use os module to list files in a dictionary 

import os

files = os.listdir()

print("Files in directory:")
for file in files:
    print(file)