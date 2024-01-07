file = "input.txt"
with open(file, 'r') as file:
    words = file.read().split()

unique_words = sorted(set(words))
for word in unique_words:
    print(word)



