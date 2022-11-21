import pandas as pd

class MovieRepositories:
    def __init__():
        print("Movie Repositories Initiated")

    def getMovieList():
        movie_data = pd.read_csv("data/movies_metadata.csv")
        movie_name = movie_data["original_title"]
        return movie_name

    def getMovies(search):
        movie_data = pd.read_csv("data/movies_metadata.csv")
        result = list(filter(lambda name: name == search, movie_data["original_title"].values.tolist()))
        print(result)
        return result