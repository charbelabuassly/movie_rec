from backend.models.recommendation.mlt_model import getmlt

def get_mlt(movie_id : int):
    most_similar = getmlt(movie_id)
    if not most_similar:
        return {
            "status": True,
            "message": "No similar movies found",
            "data": [],
        }
    else:
        # return the similar movies
        return {
            "status": True,
            "message": "Popular genres fetched",
            "data": most_similar,
        }
    
    
