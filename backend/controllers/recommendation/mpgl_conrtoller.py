from backend.models.recommendation.mpgl_model import getPopularGenres

def get_mpgh():
    genres = getPopularGenres()
    if not genres:
        return {
            "status": True,
            "message": "No popular genres found",
            "data": [],
        }
    else:
        # return the top 3
        return {
            "status": True,
            "message": "Popular genres fetched",
            "data": genres[:3],
        }
    
