# Create
my_dict = {'Name': 'Rohit', 'Age': 19 }

# Access
print(my_dict['Name'])

# Change
my_dict['Age'] = 26
my_dict['Location'] = 'India'

# Remove
del my_dict['Location']
print(my_dict)

# Update
another_dict = {'Salary': 5000, 'Nationality': 'Indian'}
my_dict.update(another_dict)
print(my_dict)

# Clear
my_dict.clear()
print(my_dict)

# Delete
del my_dict


