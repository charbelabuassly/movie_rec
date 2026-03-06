from pydantic import BaseModel

class MovieToWatchList(BaseModel): #Can be used for both the Add to watchlist, and remove
    movieId : int
    
class Watched(BaseModel): #Will be used when the movie is marked as watched
    movieId : int
    rating : float
    tags : str 
    

