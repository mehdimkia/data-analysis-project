import pandas as pd

# Load the Excel file
file_path = 'unemploymnt rate.xlsx'
xls = pd.ExcelFile(file_path)

# Load the relevant sheet and skip unnecessary rows
df_cleaned = pd.read_excel(xls, sheet_name='Sheet 1', skiprows=7, header=None)

# Rename columns with a default range for easier manipulation
df_cleaned.columns = range(df_cleaned.shape[1])

# Filter out the relevant rows and columns (years 2015 to 2021 and country names)
df_years = df_cleaned.loc[4:, [0, 3, 5, 7, 9, 11, 13, 15]]
df_years.columns = ['Country', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

# Convert the data to numeric where appropriate, handling non-numeric values
df_years.iloc[:, 1:] = df_years.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Calculate the average unemployment rate from 2015 to 2021 for each country and round to two decimals
df_years['Average'] = df_years.iloc[:, 1:].mean(axis=1).round(2)

# Save the updated dataframe to a new Excel file
#output_file_path = 'path_to_your_file/unemployment_data_with_average.xlsx'
print(df_years.head())
df_years.to_csv("unemployment_data_with_averages.csv", index=False)

# df_years.to_excel(output_file_path, index=False)

#print(f"File saved to {output_file_path}")
