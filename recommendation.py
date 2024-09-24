import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# list of movies with genres and movie IDs
movies = [
    {'movie_id': 1, 'title': 'Inception', 'genre': 'Sci-Fi'},
    {'movie_id': 2, 'title': 'The Matrix', 'genre': 'Sci-Fi'},
    {'movie_id': 3, 'title': 'Interstellar', 'genre': 'Sci-Fi'},
    {'movie_id': 4, 'title': 'The Godfather', 'genre': 'Crime'},
    {'movie_id': 5, 'title': 'The Dark Knight', 'genre': 'Action'},
    {'movie_id': 6, 'title': 'Pulp Fiction', 'genre': 'Crime'},
    {'movie_id': 7, 'title': 'Schindler\'s List', 'genre': 'Drama'},
    {'movie_id': 8, 'title': 'The Shawshank Redemption', 'genre': 'Drama'},
    {'movie_id': 9, 'title': 'Avengers: Endgame', 'genre': 'Action'},
    {'movie_id': 10, 'title': 'Gladiator', 'genre': 'Action'}
]

# Movie ratings data for collaborative filtering
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
    'movie_id': [1, 2, 3, 1, 4, 2, 3, 4, 1, 4],
    'rating': [4, 5, 3, 5, 4, 3, 4, 2, 5, 4]
}

ratings = pd.DataFrame(data)

# Creating a user-item matrix for collaborative filtering
user_item_matrix = ratings.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
user_item_sparse = csr_matrix(user_item_matrix)

# Compute cosine similarity between items (movies)
item_similarity = cosine_similarity(user_item_sparse.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# Function to recommend movies based on genre (simple recommendation)
def recommend_movies_by_genre(genre):
    recommended_movies = [movie['title'] for movie in movies if movie['genre'].lower() == genre.lower()]
    if recommended_movies:
        print(f"Based on your interest in {genre} movies, we recommend you to watch:")
        for movie in recommended_movies:
            print(f"- {movie}")
    else:
        print(f"Sorry, we don't have any movies listed under the genre '{genre}'.")

# Function to recommend movies based on similarity (content-based filtering)
def recommend_movies_by_similarity(movie_id, num_recommendations=3):
    if movie_id not in item_similarity_df.columns:
        print(f"Movie with ID {movie_id} not found!")
        return

    similar_items = item_similarity_df[movie_id].sort_values(ascending=False).iloc[1:num_recommendations+1]
    movie_titles = []
    for sim_movie_id in similar_items.index:
        movie_title = next((m['title'] for m in movies if m['movie_id'] == sim_movie_id), None)
        if movie_title:
            movie_titles.append(movie_title)
    return movie_titles

# Ask the user for their preferred genre
user_genre = input("What genre of movie would you like to watch? (e.g., Action, Drama, Sci-Fi, Crime): ")

# Recommend movies based on genre
recommend_movies_by_genre(user_genre)

# Ask the user if they want personalized recommendations based on a movie they liked
movie_id_input = input("Enter the movie ID you liked to get similar movie recommendations (or type 'none' to skip): ")

if movie_id_input.lower() != 'none':
    try:
        movie_id = int(movie_id_input)
        similar_movies = recommend_movies_by_similarity(movie_id, num_recommendations=3)
        if similar_movies:
            print(f"Since you liked movie ID {movie_id}, we recommend you to watch:")
            for movie in similar_movies:
                print(f"- {movie}")
    except ValueError:
        print("Invalid movie ID entered!")
