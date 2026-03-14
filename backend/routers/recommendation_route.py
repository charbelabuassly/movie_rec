from fastapi import APIRouter, Depends
from backend.utils.user_authorization import get_current_user
from backend.controllers.recommendation.mpoat_controller import getMPOAT
from backend.controllers.recommendation.mpgl_conrtoller import get_mpgh
from backend.controllers.recommendation.get_top_genre_movies_conrtoller import getTopMoviesPerGenre
recommendation_router = APIRouter()


#Router for popular movies
@recommendation_router.get('/popularMovies')
async def get_popular_movies(user : str = Depends(get_current_user)):
    return getMPOAT()

#Router for most popular genres, the result of this api will be used in the API below
@recommendation_router.get('/popularGenres')
async def get_popular_genres(user : str = Depends(get_current_user)):
    return get_mpgh()

#Get most popular movies for this specific genres
@recommendation_router.get('/topGenreMovies/{genre_id}')
async def get_top_genre_movies(genre_id : int, user : str = Depends(get_current_user)):
    return getTopMoviesPerGenre(genre_id) 

