import pandas as pd

data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [23, 45, 32, 25],
    "City": ["New York", "Paris", "Berlin", "London"],
}
df = pd.DataFrame(data)

print(df)
