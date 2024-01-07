# WAP that input a text file. the program sghould print all of the 
# unique words in the file in alphabetical order.
import re 
file_path = "new_file.txt"
content = '''Rohit , 90 , 80  , 90
Utpal , 90 , 80 , 70
Shivang , 80 , 70 , 60
Rahul , 90 , 60 , 30'''
file = open(file_path , "w")
file.write(content)
file.close()

# read the content of the file
# file = open(file_path , "r")
# print(file.read())
# file.close()

# Calculate the average score of each student
file = open(file_path , "r")
list = []
for x in file:
  list.append(x)
file.close()

print(list[0])
x = re.findall(r"\d+",list[0])
print(x)
sum = 0
for i in x:
  sum += int(i)

print(sum)