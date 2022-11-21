from fastapi import FastAPI
from src.controllers.movieControllers import MovieController
app = FastAPI()

@app.get("/")
def test():
    return { "Hello world!" }

@app.get("/getMovieList")
def getMovieList():
    result = MovieController.getMovieList()
    return result

@app.get("/getMovies")
def getMovies(search):
    result = MovieController.getMovies(search)
    return result
