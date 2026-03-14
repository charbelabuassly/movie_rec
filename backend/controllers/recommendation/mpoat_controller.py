from backend.models.recommendation.mpoat_model import getMPOAT as getMPOATModel

def getMPOAT():
    mpoat = getMPOATModel()
    if not mpoat:
        return {
            "status": True,
            "message": "No popular movies found",
            "data": [],
        }
    else:
        return {
            "status": True,
            "message": "Popular movies fetched",
            "data": mpoat,
        }
    
