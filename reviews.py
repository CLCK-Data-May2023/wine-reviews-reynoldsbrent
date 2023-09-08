# add your code here
import pandas as pd

# Read the data from the CSV file
data = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# Group the data by country and calculate the count and average points
summary = data.groupby('country').agg({'points': ['count', 'mean']}).round(1)

# Reset the index to make 'country' a column again
summary.reset_index(inplace=True)

# Rename the columns to 'country', 'count', and 'points'
summary.columns = ['country', 'count', 'points']

# Write the summary data to a new CSV file
summary.to_csv('data/reviews-per-country.csv', index=False)

# Print the first few rows of the summary
print(summary.head())