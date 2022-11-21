from src.logics.movieBusinessLogics import MovieBusinessLogics

class MovieController:
    def searchMovies(query: str):
        return MovieBusinessLogics.searchMovies(query)

    def findMovie(movie_id: str):
        return MovieBusinessLogics.findMovie(movie_id)