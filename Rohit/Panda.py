import pandas as pd

data = {'name': ['Rohit', 'Rahul', 'Amit'],
        'marks': [78, 85, 90]}

df = pd.DataFrame(data)

admission_nos = [101, 102, 103]
df['admission_no'] = admission_nos

print(df)
