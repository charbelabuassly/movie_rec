from backend.controllers.movies.movies_controller import addMovies, removeMovie, setWatched
from fastapi import APIRouter, Depends
from backend.schemas.movie_schema import MovieToWatchList, Watched
from backend.utils.user_authorization import get_current_user
#This page will handle all user related urls. Like Login , Login etc
    
    
movies_router = APIRouter()

@movies_router.post('/addWatchlist')
async def addToWatchList(movieData : MovieToWatchList, user = Depends(get_current_user)):
    return addMovies(movieData, user)

@movies_router.post('/removeWatchList')
async def removeFromWatchList(movieData : MovieToWatchList, user = Depends(get_current_user)):
    return removeMovie(movieData, user)

@movies_router.post('/markWatched')
async def markWatched(movieData : Watched,  user = Depends(get_current_user)):
    return setWatched(movieData, user)
