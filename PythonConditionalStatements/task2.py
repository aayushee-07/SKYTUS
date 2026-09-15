# grade calculator based on marks 90+= A, 80+= B, 70+= C 

marks= int(input("Enter your marks:"))

if marks >= 90:
    print("Grade A")

elif marks>=80:
    print("Grade B")

elif marks>=70:
    print("Grade C")

elif marks>=60:
    print("Grade D")

elif marks>=50:
    print("Grade E")

elif marks>=40:
    print("Pass")

else:
    print("Fail")
