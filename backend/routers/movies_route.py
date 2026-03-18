from backend.controllers.movies.movies_controller import addMovies, removeMovie, setWatched, getWatchList
from fastapi import APIRouter, Depends
from backend.schemas.movie_schema import MovieToWatchList, Watched
from backend.utils.user_authorization import get_current_user

#This will handle all watchlist related operations
    
    
movies_router = APIRouter()

@movies_router.post('/addWatchlist')
def addToWatchList(movieData : MovieToWatchList, user = Depends(get_current_user)):
    return addMovies(movieData, user)

@movies_router.post('/removeWatchList')
def removeFromWatchList(movieData : MovieToWatchList, user = Depends(get_current_user)):
    return removeMovie(movieData, user)

@movies_router.post('/markWatched')
def markWatched(movieData : Watched,  user = Depends(get_current_user)):
    return setWatched(movieData, user)

@movies_router.get('/displayWatchlist')
def displayWatched(user = Depends(get_current_user)):
    return getWatchList(user)
