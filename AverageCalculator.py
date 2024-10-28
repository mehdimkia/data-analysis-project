# Import necessary libraries
import pandas as pd

# Load the Excel file
file_path = "/Users/mkia/PycharmProjects/pythonProject/tps00122_page_spreadsheet (1).xlsx"  # Replace this with your actual file path
df = pd.read_excel(file_path, sheet_name="Sheet 1", skiprows=10)

# Clean the data by removing irrelevant "Unnamed" columns
df_cleaned = df.drop(columns=[col for col in df.columns if "Unnamed" in col])

# Select only the relevant columns from 2015 to 2021
columns_of_interest = ['TIME', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
df_filtered = df_cleaned[columns_of_interest]

# Convert all columns except 'TIME' to numeric (handle non-numeric entries if needed)
df_filtered.iloc[:, 1:] = df_filtered.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Calculate row-wise averages for the selected years (2015-2021)
df_filtered['average'] = df_filtered.iloc[:, 1:].mean(axis=1)

df_filtered['average'] = df_filtered['average'].round(2)

# Save the resulting dataframe to a new CSV file (or Excel file if preferred)
df_filtered.to_csv("data_with_averages.csv", index=False)

# Print the first few rows of the result
print(df_filtered.head())
