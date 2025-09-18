import pandas as pd
import plotly.express as px

# Reading the CSV file
df = pd.read_csv('CSVS/Albums and their genres amount.csv')  

# Selecting the genres that are going to be included in the pie chart and the amount of albums under that genre
genres_included = ['Hip Hop', 'Rock', 'Jazz', 'Country', 'Folk','Electronic', 'Rap','Metal', 'Ambient', 'Neo-Psychedelia', 'Samba', 'MPB', 'Fusion', 'Chiptune', 'Synthpop']

# Sum values for each column
values = df[genres_included].sum()

# Create a pie chart
fig = px.pie(
    names = values.index,  # Column names as labels
    values = values.values,  # Summed values as data
    title = '500 Albums And Their Genres'
)

# Show the plot
fig.show()
