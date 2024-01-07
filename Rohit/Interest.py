def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time):
    return principal * (pow((1 + rate / 100), time))

p = int(input("Enter Principal : "))
r = int(input("Enter Rate : "))
t = int(input("Enter Year(in years) : "))

print("Simple Interest : %.2f" % simple_interest(p,r,t))
print("Compound Interest : %.2f" % compound_interest(p,r,t))


