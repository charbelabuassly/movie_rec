from fastapi import APIRouter, Depends
from backend.utils.user_authorization import get_current_user
from backend.controllers.recommendation.mpoat_controller import getMPOAT
from backend.controllers.recommendation.mpgl_controller import get_mpgh
from backend.controllers.recommendation.get_top_genre_movies_controller import getTopMoviesPerGenre
from backend.controllers.recommendation.mlt_conrtoller import get_mlt
from backend.schemas.user.user_schema import User
recommendation_router = APIRouter()


#Router for popular movies
@recommendation_router.get('/popularMovies')
def get_popular_movies(user : User = Depends(get_current_user)):
    return getMPOAT()

#Router for most popular genres, the result of this api will be used in the API below
@recommendation_router.get('/popularGenres')
def get_popular_genres(user : User = Depends(get_current_user)):
    return get_mpgh()

#Get most popular movies for this specific genres
@recommendation_router.get('/topGenreMovies/{genre_id}')
def get_top_genre_movies(genre_id : int, user : User = Depends(get_current_user)):
    return getTopMoviesPerGenre(genre_id)

#Get the most similar movies to a designated movie
@recommendation_router.get('/moreLikeThis/{movie_id}')
def get_more_like_this(movie_id, user : User = Depends(get_current_user)):
    return get_mlt(movie_id)