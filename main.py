from fastapi import FastAPI
from src.controllers.movieControllers import MovieController
app = FastAPI()

class Response:
    def __init__(self, code, data):
        self.code = code
        self.data = data

    def __str__(self):
        return { "code": self.code, "data": self.data }

"""
For page(s):
    /search
    /searchResult
"""
@app.get("/search")
def searchMovies(query: str):
    result = MovieController.searchMovies(query)
    response = Response(200, result) if result else Response(500, None)
    return response

"""
For page:
    /movieDetail
"""
@app.get("/movies/{movie_id}")
def findMovie(movie_id: str):
    result = MovieController.findMovie(movie_id)
    response = Response(200, result) if result else Response(500, None)
    return response

# """
# For page:
#     /actorDetail
# """
# @app.get("/actors/{actor_id}")
# def findActor(actor_id: str):
#     return {"Placeholder"}

# """
# For page:
#     /newMovie
# """
# @app.post()

# """
# For page:
#     /signIn
# """
# @app.post()