import pandas as pd

class MovieRepositories:
    def searchMovies(query: str):
        raw_movie_data = pd.read_csv("data/movies_metadata.csv")
        movie_name = raw_movie_data["original_title"]
        result = movie_name.loc[movie_name.eq(query)].tolist()
        return result

    def findMovie(movie_id: str):
        raw_movie_data = pd.read_csv("data/movies_metadata.csv")
        movie_detail = raw_movie_data[["id", "original_title"]]
        result = movie_detail.query("id == @movie_id").values.tolist()
        return result[0]