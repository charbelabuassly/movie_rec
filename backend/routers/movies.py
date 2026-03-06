from backend.controllers.movies import addMovies, removeMovie, setWatched
from fastapi import APIRouter, Depends
from backend.schemas.movie_schema import MovieToWatchList, Watched
from pydantic import EmailStr
from backend.utils.jwt_handler import get_user
#This page will handle all user related urls. Like Login , Login etc
    
    
movies_router = APIRouter()

@movies_router.post('/addWatchlist')
async def addToWatchList(movieData : MovieToWatchList, email : EmailStr = Depends(get_user)):
    return addMovies(movieData, email)

@movies_router.post('/removeWatchList')
async def removeFromWatchList(movieData : MovieToWatchList, email : EmailStr = Depends(get_user)):
    return removeMovie(movieData, email)

@movies_router.post('/markWatched')
async def markWatched(movieData : Watched,  email : EmailStr = Depends(get_user)):
    return setWatched(movieData, email)