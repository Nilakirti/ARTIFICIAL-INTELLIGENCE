import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Define a dataset of movies
movies = pd.DataFrame({
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'genre': ['Action, Thriller', 'Comedy, Romance', 'Action, Adventure', 'Thriller, Horror', 'Comedy, Drama'],
    'description': ['Fast-paced action movie', 'Funny romantic comedy', 'Exciting adventure movie', 'Scary thriller movie', 'Emotional drama movie']
})

# Define a TF-IDF vectorizer to convert text data into vectors
vectorizer = TfidfVectorizer(stop_words='english')

# Fit the vectorizer to the movie descriptions and transform them into vectors
movie_vectors = vectorizer.fit_transform(movies['description'])

# Calculate the similarity between movies using cosine similarity
similarity_matrix = linear_kernel(movie_vectors, movie_vectors)

# Define a function to make recommendations for a movie
def make_recommendations(movie_title, num_recommendations):
    # Get the index of the movie
    movie_index = movies[movies['title'] == movie_title].index[0]

    # Get the similarity scores for the movie
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    # Sort the similarity scores in descending order
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    # Get the indices of the most similar movies
    most_similar_movies = [i[0] for i in similarity_scores[1:num_recommendations + 1]]

    # Return the titles of the most similar movies
    return movies['title'].iloc[most_similar_movies]

# Make recommendations for 'Movie A'
recommended_movies = make_recommendations('Movie A', 2)
print("Recommended movies for 'Movie A':", recommended_movies.values)