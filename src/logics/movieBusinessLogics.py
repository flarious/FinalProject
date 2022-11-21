from src.repositories.movieRepositories import MovieRepositories

class MovieBusinessLogics:
    def searchMovies(query: str):
        return MovieRepositories.searchMovies(query)

    def findMovie(movie_id: str):
        return MovieRepositories.findMovie(movie_id)