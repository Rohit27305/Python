print("Enter three numbers : ")
a = int(input())
b = int(input())
c = int(input())
if a>b:
  if a>c:
    print("a is the greatest ",a)
  else:
    print("c is the greatest ",c)
elif b>c:
  print("b is the greatest ",b)
else:
  print("c is the greatest ",c)