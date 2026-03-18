# ------------------------------
# MOST POPULAR MOVIES FOR GENRE
# ------------------------------

"""
In this section the most popular movies for a specific given genre will be returned
"""

from backend.database.database import cnx

def getTopGenreMovies(genre_id : int):
    query = """
        select m.movie_id, m.weighted_rating from
        movies m
        inner join movie_genre mg on mg.movie_id = m.movie_id
        where mg.genre_id = (%s) order by m.weighted_rating desc 
        limit 50
    """
    cur = cnx.cursor(dictionary=True, buffered= True)
    cur.execute(query, (genre_id,))
    tmpg = cur.fetchall()
    cur.close()
    return tmpg # will return none if nothing

