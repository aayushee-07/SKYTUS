# write program to handle indexerror when accessing a list 

try:
    list=["aayushee",1,3,5,7,"riya"]

    print(list[10])

except IndexError:
    print("There is an index error!,plase try again")