# Data Analysis Project

This repository contains Python scripts developed as part of my postgraduate coursework, where I explored data analysis using Python. I’ve included sample data and detailed instructions to demonstrate how each script operates. 

## Project Overview

This project includes scripts for analyzing various datasets, including GDP, unemployment rates, and other economic indicators. The main tasks involve calculating averages, performing linear projections, and analyzing correlations. Each script is self-contained and performs a specific function on provided sample datasets.


## Scripts Description

### `AverageCalculator.py`
This script reads a data file, calculates the average value for each row, and inserts the results in a new column labeled "average."

### `AverageForGDP.py`
Calculates the average GDP for each row in a GDP data file, focusing on values from 2015 to 2021. The results are saved in a new CSV file with the average GDP per country.

### `AverageUnemploymentRate.py`
Processes a dataset with unemployment rates and calculates the average unemployment rate from 2015 to 2021 for each row.

### `LinearProjection.py`
Projects a linear trend based on historical data in the dataset, which can be used to estimate future values.

### `AlcoholConsumption.py`
Analyzes alcohol consumption rates per country from a given dataset and provides insights into consumption trends.

### `CorrelationAnalysis.py`
Performs a correlation analysis between selected indicators, allowing for insights into relationships between different economic or social indicators.

## Sample Data

The `sample_data/` folder includes example data files that can be used to run the scripts. These are smaller, representative datasets extracted from the original data files. Each file includes data for the years 2015 to 2021.

## How to Run the Scripts

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-analysis-project.git
   cd data-analysis-project

2. (Optional) Create and activate a virtual environment:
    ```bash    
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows

3. Install dependencies:
    ```bash    
        pip install pandas
   
4. Run any script:
    ```bash    
        python AverageCalculator.py

## Acknowledgments
I’d like to thank Dr. Rok Hrzic, for providing the opportunity to explore data analysis through this project. I’ve learned valuable skills in data manipulation, analysis, and Python programming.