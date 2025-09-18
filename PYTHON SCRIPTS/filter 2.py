import pandas as pd


df = pd.read_csv('CSVS/filtered_aoty.csv')

# Keywords to sort subgenres under the one genre
keywords = ['Hip Hop', 'Rock', 'Pop', 'Jazz', 'Country', 'Folk', 'Electronic', 'Rap', 'Indie', 'Classical']

# Keep track of the genres that have already been detected
detected_genres = set()

# Loop through the keywords to find rows a column contains a keyword
for keyword in keywords:
    # Printing to make sure which keywords are being filtered currently
    print(f"Checking for '{keyword}'...")
    
    # Filtering any row where a column contains the keyword
    matching_rows = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(), axis=1)]
    
    # Printing the rows that match the keywords (only if they haven't been detected yet)
    for index, row in matching_rows.iterrows():
        genre = keyword  # Always use the main genre name (e.g., 'Hip Hop','Rock', 'Electronic')
        if genre not in detected_genres:
            print(f"\nFound genre: {genre}")
            print(row)
            detected_genres.add(genre)

# Saving the filtered data to a new CSV File
df.to_csv('HTML_graphData.csv', index=False)
print("Filtered results saved to 'HTML_graphData.csv'.")
