# Data manipulation library
import pandas as pd

# This will clean the CSV file and creates a new one
df = pd.read_csv('train.csv')

# shows top 6 unique category based on the column "Name"
top_categories = df['Customer Name'].value_counts().head(6)
#print(top_categories)

#shows last row of DataFrame
#print(df.tail(6))

# Shows total row count
total_rowcount = len(df)
print(f"Number of rows: {total_rowcount}")

# Viewing specific columns
selected_columns = df[['Customer Name', 'Segment']]
print(selected_columns)

# Remove duplicates based on all columns (default behavior)
new_df = df.drop_duplicates()
print("\nDataFrame after removing duplicates (all columns):")
print(new_df)

# Remove all occurrences of duplicate rows
# (if a row appears more than once, all instances are removed)
# For a sorted unique series
new_df_all_removed = df['Customer Name'].drop_duplicates().sort_values()
print("\nDataFrame after removing ALL duplicates:")
print(new_df_all_removed)

# Modify the DataFrame in place
df.drop_duplicates(inplace=True)
print("\nOriginal DataFrame after in-place modification:")
print(df)

# Records by Segment
# Get unique and sorted values from a Series (e.g., 'Segment')
unique_sorted_series = df['Segment'].unique()
unique_sorted_series.sort()
#unique_sorted_series.to_csv('clean_train.csv', index=False)
print("\nUnique sorted Series:")
print(unique_sorted_series)

