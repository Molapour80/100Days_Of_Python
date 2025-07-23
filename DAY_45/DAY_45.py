import pandas as pd
import zipfile
import requests
import os

url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
save_path = "ml-latest-small.zip"


response = requests.get(url)
with open(save_path, 'wb') as f:
    f.write(response.content)


with zipfile.ZipFile(save_path, 'r') as zip_ref:
    zip_ref.extractall(".")


print("file:", os.listdir("ml-latest-small"))

imdb_ratings_url = "https://datasets.imdbws.com/title.ratings.tsv.gz"
imdb_basics_url = "https://datasets.imdbws.com/title.basics.tsv.gz"

ratings = pd.read_csv("ml-latest-small/ratings.csv")
movies = pd.read_csv("ml-latest-small/movies.csv")

print(ratings.head()) 
print(movies.head())

print("count rating:", len(ratings))
print("count movies:", len(movies))


print(movies.info())
print(ratings.describe())

movies['genres'] = movies['genres'].str.split('|')
genres_expanded = movies['genres'].explode()
genres_encoded = pd.get_dummies(genres_expanded).groupby(level=0).sum()

movies = pd.concat([movies, genres_encoded], axis=1)

#######################################


