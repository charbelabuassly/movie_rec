from fastapi import HTTPException
from backend.models.users import get_user_by_email
from backend.models.movies import checkMovie, addMovie as addMovieModel, removeMovie as removeMovieModel, setWatched as setWatchedModel
from backend.models.tags import insert_tag
from backend.models.ratings import insert_rating

def addMovies(movieData, email) -> dict:
    user = get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="Account Not Found")
    else:
        user_id = user['user_id'] #grabbing the user_id
        movie_id = movieData.movieId #grabbing the movie_id
        
        #We need to check if the movie exists or not
        status = checkMovie(movie_id)
        if not status:
            raise HTTPException(status_code=404, detail="Movie Not Found")
        else:
            addMovieModel(movie_id, user_id)
            return {"status" : "Movie Added Successfully"}
            
        
def removeMovie(movieData, email) -> dict:
    user = get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="Account Not Found")
    else:
        user_id = user['user_id']
        movie_id = movieData.movieId #grabbing the movie_id
        
        #We need to check if the movie exists or not
        status = checkMovie(movie_id)
        if not status:
            raise HTTPException(status_code=404, detail="Movie Not Found")
        else:
            removeMovieModel(movie_id, user_id)
            return {"status" : "Movie Removed Successfully"}
            
def setWatched(movieData, email) -> dict:
    movie_id = movieData.movieId
    rating = movieData.rating
    tags = movieData.tags
    user = get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="Account Not Found")
    else:
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
            return {"status" : "Movie set as watched"}
