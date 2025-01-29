import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'ds_salaries.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

print(df.head())

df["remote_ratio"].max()

sorted = df["salary_in_usd"].sort_values()
sorted.tail()
print(sorted)

remote = df.query("remote_ratio == 100")
print(remote)
print(len(remote))