import pandas as pd
import plotly.express as px

# Load the CSV file
csv_path = 'CSVS/filtered_aoty.csv'
df = pd.read_csv(csv_path)

# Use a dictionary to store artist album counts
artist_album_counts = {}

# Iterate through the dataset to fill the dictionary
for artist in df['artist']:
    artist_album_counts[artist] = artist_album_counts.get(artist, 0) + 1  # Increment count

# Convert dictionary to a sorted list of tuples (artist, num_albums)
sorted_artists = sorted(artist_album_counts.items(), key=lambda x: x[1], reverse=True)
        
# Convert the sorted data to a DataFrame for visualisation
top_n = 10  # Number of top artists to display
top_artists_df = pd.DataFrame(sorted_artists[:top_n], columns=['artist', 'num_albums'])

# Create a bar chart using Plotly
fig = px.bar(
    top_artists_df,
    x='artist',
    y='num_albums',
    title='Top 10 Artists by Number of Albums in the Dataset',
    labels={'artist': 'Artist', 'num_albums': 'Number of Albums'},
    color='num_albums', 
    color_continuous_scale='Viridis'
)

# Show the plot
fig.show()
