import numpy as np
import pandas as pd

# Parameters for data generation
mean_rubbish_count = 600
mean_direction = 270
mean_wind_speed = 0.55

# Variability percentages
variability_percentage = 0.20

# Number of samples to generate
num_samples = 10

# Standard deviation calculation for variability
std_dev_rubbish_count = mean_rubbish_count * variability_percentage
std_dev_direction = mean_direction * variability_percentage
std_dev_wind_speed = mean_wind_speed * variability_percentage

# Generate data with variability
rubbish_count_data = np.random.normal(loc=mean_rubbish_count, scale=std_dev_rubbish_count, size=num_samples)
direction_data = np.random.normal(loc=mean_direction, scale=std_dev_direction, size=num_samples)% 360
wind_speed_data = np.random.normal(loc=mean_wind_speed, scale=std_dev_wind_speed, size=num_samples)

# Constant data for region
region_data = np.zeros(num_samples)

# Create a DataFrame to organize the data
df = pd.DataFrame({
    'Rubbish Count': rubbish_count_data,
    'Region': region_data,
    'Direction': direction_data,
    'Wind Speed': wind_speed_data
})

# Display the first few rows of the DataFrame
print(df.head())