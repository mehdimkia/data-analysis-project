# Import necessary libraries
import pandas as pd

# Load the Excel file
gdp_file_path = "unemploymnt rate.xlsx"  # Replace this with your actual file path
gdp_data = pd.read_excel(gdp_file_path, sheet_name='Sheet')

# Clean the data by removing irrelevant "Unnamed" columns
gdp_cleaned = gdp_data.drop(columns=[col for col in gdp_data.columns if "Unnamed" in col])

# Convert GDP values to numeric (remove commas)
gdp_cleaned.iloc[:, 1:] = gdp_cleaned.iloc[:, 1:].replace({',': ''}, regex=True).apply(pd.to_numeric, errors='coerce')

# Calculate row-wise averages for the selected years (2015-2021)
gdp_cleaned['average'] = gdp_cleaned.iloc[:, 1:].mean(axis=1)

# Round the 'average' column to 2 decimal places
gdp_cleaned['average'] = gdp_cleaned['average'].round(1)

# Save the resulting dataframe to a new CSV file (or Excel file if preferred)
gdp_cleaned.to_csv("gdp_data_with_averages.csv", index=False)

# Print the first few rows of the result
print(gdp_cleaned.head())
