my_dict = {'b': 5, 'a': 10, 'c': 8, 'd': 20}

# Ascending
asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(asc)

# Descending
desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(desc)
