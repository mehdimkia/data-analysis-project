import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Data
data = {
    'Country': ['Finland', 'Norway', 'Sweden', 'Italy', 'Spain', 'Greece'],
    'Suicide Rate': [13.86, 12.12, 12.23, 5.81, 7.55, 4.46],
    'PCI Score': [9, 7, 5, 3, 3, 1],
    'GDP per Capita (US$)': [47759, 77492, 54012, 32895, 28273, 18774],
    'Unemployment Rate (%)': [8.1, 4.43, 7.46, 10.61, 16.96, 20.09],
    'Alcohol Consumption (Liters)': [9.21, 6.94, 9.39, 7.65, 10.04, 6.88]
}

# Create DataFrame
df = pd.DataFrame(data)


# Function to calculate Pearson Correlation Coefficient, plot scatter plot and best fit line
def calculate_and_plot(x, y, x_label, y_label):
    # Calculate Pearson correlation coefficient
    corr, _ = pearsonr(x, y)
    print(f"Pearson correlation between {x_label} and {y_label}: {corr:.3f}")

    # Scatter plot
    plt.scatter(x, y, label='Data points')

    # Add line of best fit
    m, b = np.polyfit(x, y, 1)  # m is the slope, b is the intercept
    plt.plot(x, m * x + b, color='red', label=f'Best fit line (slope={m:.2f})')

    # Add titles and labels
    plt.title(f"{x_label} vs {y_label}")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()


# Calculate and plot for each pair
calculate_and_plot(df['Suicide Rate'], df['PCI Score'], 'Suicide Rate', 'PCI Score')
calculate_and_plot(df['Suicide Rate'], df['GDP per Capita (US$)'], 'Suicide Rate', 'GDP per Capita (US$)')
calculate_and_plot(df['Suicide Rate'], df['Unemployment Rate (%)'], 'Suicide Rate', 'Unemployment Rate (%)')
calculate_and_plot(df['Suicide Rate'], df['Alcohol Consumption (Liters)'], 'Suicide Rate',
                   'Alcohol Consumption (Liters)')
