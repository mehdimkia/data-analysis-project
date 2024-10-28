import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating a dataframe manually from the provided data
data = {
    'Country': ['Greece', 'Italy', 'Spain', 'Norway', 'Sweden', 'Finland'],
    '2015': [7.5, 7.7, 9.9, 6.8, 9.4, 9.4],
    '2016': [7.3, 7.6, 10.9, 6.8, 9.4, 9.3],
    '2017': [7.3, 7.8, 10.9, 6.8, 9.3, 9.2],
    '2018': [7.1, 8, 10.9, 6.8, 9.3, 9.2],
    '2019': [7.1, 8, 10.9, 6.8, 9.3, 9.2],
    '2020': [5.8, 7, 9.2, 7.4, 9.6, 9.1]
}

df = pd.DataFrame(data)

# Fixing the extrapolation to ignore NaN values for now
for country in df['Country']:
    # Extract the values for each country (ignore NaNs)
    values = df[df['Country'] == country].iloc[0, 1:].dropna().values.astype(float)

    # Check if lengths match
    if len(values) == 6:  # Ensure there are 6 years of data (2015-2020)
        # Perform linear extrapolation
        years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
        slope, intercept = np.polyfit(years, values, 1)
        extrapolated_value_2021 = slope * 2021 + intercept

        # Adding the extrapolated value to the dataframe
        df.loc[df['Country'] == country, '2021'] = extrapolated_value_2021
    else:
        print(f"Data length mismatch for {country}: {len(values)} values found.")

# Display the dataframe with extrapolated values
print(df)

# Plotting the trends and extrapolated 2021 values
plt.figure(figsize=(10, 6))
for country in df['Country']:
    plt.plot(df.columns[1:], df[df['Country'] == country].iloc[0, 1:], marker='o', label=country)

# Moving the legend outside the plot
plt.title('Alcohol Consumption Per Capita (Liters of Pure Alcohol) 2015-2021')
plt.xlabel('Year')
plt.ylabel('Alcohol Consumption (Liters)')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()  # Adjust layout to accommodate the legend
plt.show()
