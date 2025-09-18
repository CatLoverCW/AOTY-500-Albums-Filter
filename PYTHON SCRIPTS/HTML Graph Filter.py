import pandas as pd

# Reading the CSV file
df = pd.read_csv("CSVS/filtered_aoty.csv")

# Keywords of genres that will cause all subgenres to fall under one genre 
keywords = ['Hip Hop', 'Rock', 'Pop', 'Jazz', 'Country', 'Folk', 'Electronic', 'Rap', 'Metal', 'Ambient', 'Neo-Psychedelia', 'Krautrock', 'Samba', 'MPB', 'Samba-rock',  'Fusion', 'Chiptune', 'Synthpop']

# Keep track of the genres that have already been detected
detected_genres = set(keywords)

# Dictionary to keep track of the count of albums for each genre (Will be used in graph)
genre_counts = {keyword: 0 for keyword in keywords}

# Loop through the keywords to find rows a column contains a keyword
for keyword in keywords:
    print(f"Checking for keyword: {keyword}") 
   
    # Filtering any row where a column contains a keyword
    matching_rows = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(), axis=1)]
    
    # Counting the amount of albums that fall under each genre
    genre_counts[keyword] = matching_rows.shape[0]
    
    # Loop through each matching row
    for index, row in matching_rows.iterrows():
        genre = row['genres']
        
# Create a new DataFrame with the genres and the amount of albums that fall under (I will then turn this DataFrame into a CSV file)
genre_count_df = pd.DataFrame(list(genre_counts.items()), columns=['Genre', 'Album Count'])

# Saving the filtered data to a new CSV File
genre_count_df.to_csv('HTML_graphData.csv', index=False)
print("Filtered results saved to 'HTML_graphData.csv'.")
