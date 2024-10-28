import pandas as pd

# Load the Excel file
file_path = 'Alcohol Consumption.xlsx'
xls = pd.ExcelFile(file_path)

# Load the relevant sheet
df_cleaned = pd.read_excel(xls, sheet_name='Sheet1')

# Calculate the average values from 2015 to 2021 for each country and round to two decimals
df_cleaned['Average'] = df_cleaned.iloc[:, 1:].mean(axis=1).round(2)

# Save the updated dataframe to a new CSV file
output_file_path = 'alcohol_consumption_with_averages.csv'
df_cleaned.to_csv(output_file_path, index=False)

# Print the dataframe to verify
print(df_cleaned.head())
