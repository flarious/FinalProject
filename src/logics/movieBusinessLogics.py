from src.repositories.movieRepositories import MovieRepositories

class MovieBusinessLogics:
    def __init__():
        print("Movie Business Logics Initiated")

    def getMovieList():
        result = MovieRepositories.getMovieList()
        return result

    def getMovies(search):
        result = MovieRepositories.getMovies(search) if search != None else MovieRepositories.getMovieList()
        print(result)
        return result