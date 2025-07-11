import pandas as pd

# reading the csv file
movies = pd.read_csv('imdb_top_1000.csv')

# Cleaning the columns to lowercase for easy mapping of inputs
movies.columns = [col.strip().lower() for col in movies.columns]

# taking inputs
genreInput = input("Enter a genre (e.g., Drama, Action): ").lower()
minRating = float(input("Enter minimum rating (e.g., 8.0): "))

# Filtering the data
filteredMovies = movies[
    movies['genre'].str.lower().str.contains(genreInput) &
    (movies['imdb_rating'] >= minRating)
]

# Sorting on the basis of imdb ratings
topMovies = filteredMovies.sort_values(by='imdb_rating', ascending=False).head(5)
print(topMovies.columns)

if topMovies.empty:
    print("\nNo matching movies found.")
else:
    print("\nTop 5 Movie Recommendations:")
    for index, row in topMovies.iterrows():
        print(f"{row['series_title']} ({row['genre']}) - Rating: {row['imdb_rating']}")
