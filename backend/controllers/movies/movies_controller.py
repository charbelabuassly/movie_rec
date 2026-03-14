from fastapi import HTTPException
from backend.models.movies.movies_model import checkMovie, addMovie as addMovieModel, removeMovie as removeMovieModel, setWatched as setWatchedModel, displayMovies
from backend.models.movies.tags_model import insert_tag
from backend.models.movies.ratings_model import insert_rating

def addMovies(movieData, user) -> dict:
    user_id = user['user_id'] #grabbing the user_id
    movie_id = movieData.movieId #grabbing the movie_id
    
    #We need to check if the movie exists or not
    status = checkMovie(movie_id)
    if not status:
        raise HTTPException(status_code=404, detail="Movie Not Found")
    else:
        addMovieModel(movie_id, user_id)
        return {
            "status": True,
            "message": "Movie added successfully",
            "data": None,
        }
            
        
def removeMovie(movieData, user) -> dict:
    user_id = user['user_id']
    movie_id = movieData.movieId #grabbing the movie_id
    
    #We need to check if the movie exists or not
    status = checkMovie(movie_id)
    if not status:
        raise HTTPException(status_code=404, detail="Movie Not Found")
    else:
        removeMovieModel(movie_id, user_id)
        return {
            "status": True,
            "message": "Movie removed successfully",
            "data": None,
        }
            
def setWatched(movieData, user) -> dict:
    movie_id = movieData.movieId
    rating = movieData.rating
    tags = movieData.tags
    user_id = user['user_id']
    status = checkMovie(movie_id)
    if not status:
        raise HTTPException(status_code=404, detail="Movie Not Found")
    else:
        pass 
        #1-set watched using a query
        setWatchedModel(movie_id, user_id)
        #2- insert a new ratings 
        insert_rating(movie_id, rating=rating, userId= user_id)
        #3- insert a new tags if not "" 
        if tags != "":
            insert_tag(movieId=movie_id, tag=tags, userId=user_id)
        return {
            "status": True,
            "message": "Movie set as watched",
            "data": None,
        }

def getWatchList(user):
    userId = user['userId']
    movieData = displayMovies(userId)
    if not movieData:
        return {
            "status": True,
            "message": "No movies found",
            "data": [],
        }
    else:
        return {
            "status": True,
            "message": "Watchlist movies returned",
            "data": movieData
        }