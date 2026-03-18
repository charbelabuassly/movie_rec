from backend.models.recommendation.get_top_genre_movies import getTopGenreMovies

def getTopMoviesPerGenre(genre_id : int):
    tmpg = getTopGenreMovies(genre_id)
    if not tmpg:
        return {
            "status": True,
            "message": "No movies found for this genre",
            "data": [],
        }
    else:
        # return the top 3
        return {
            "status": True,
            "message": "Top genre movies fetched",
            "data": tmpg,
        }
