list = []
n = int(input("Enter no. of values : "))
print(f"Enter {n} interger value")
for i in range(n):
    temp = int(input())
    list.append(temp)
    
ans = 1
for i in list:
    ans *= i

print("Multiplication of all items :" , ans)



