list = []
n = int(input("Enter no. of values : "))
print(f"Enter {n} interger value")
for i in range(n):
    temp = int(input())
    list.append(temp)

small = list[0]
largest = list[0]

for i in list:
    if small > i:
        small = i
    if largest < i:
        largest = i

print("Smallest :",small)
print("Largest :",largest)

