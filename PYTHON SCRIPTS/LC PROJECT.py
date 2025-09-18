import pandas as pd

# Reading the csv file and making sure to only account for the first 500 rows so the CSV file is more manageable by using .iloc
df = pd.read_csv('CSVS/aoty.csv', encoding='utf-8').iloc[0:500]

# Printing the first few rows for reference
print(df.head(50))

# Remove columns from CSV file that is not needed
columns_to_remove = ["rating_count", "album_link"] 
df = df.drop(columns=columns_to_remove)

# Saving fltered data to a new  CSV file
df.to_csv("filtered_aoty.csv", index=False)
print("Filtered results saved to 'filtered_aoty.csv'.")
