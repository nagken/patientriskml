import pandas as pd

# Load the CSV
df = pd.read_csv("data/patient_data.csv")

# Print column names
print("Columns in CSV:", df.columns.tolist())

# Print first few rows to check structure
print(df.head())
