
# WAPP to double a given number and add two numbers using lambda()

add = lambda x,y : x+y

num1 = int(input("Enter a first Number : "))
num2 = int(input("Enter a second Number : "))

result1 = add(num1 , num2)
print("After Addition " , result1)

double = lambda x : x*2
num = int(input("Enter number :"))

print("After double : " , float(double(num)))