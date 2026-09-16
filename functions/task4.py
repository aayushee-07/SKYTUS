# fun to find simple intrest 

def simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI


P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
T = float(input("Enter time: "))

print("Simple Interest =", simple_interest(P, R, T))