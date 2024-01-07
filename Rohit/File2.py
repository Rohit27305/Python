# i
with open("example.txt", "w") as file:
    file.write("hello world")
    
# ii
with open("example.txt", "a") as file:
    file.write(" hi python programming")

file = open("example.txt", "r")
for word in file:
    print(word)

    
