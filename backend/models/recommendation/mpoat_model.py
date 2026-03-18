# -------------------------
# MOST POPULAR OF ALL TIME
# -------------------------

"""
Most popular movies will be chosen based on the ones with the most user interactions
and highest weighted ratings. No time constraints. 

In order to make the query as optimized as possible, we will choose the most popular
based on the highest weighted ratings. Weighted ratings will be updated with every batch update, 

"""

from backend.database.database import cnx

def getMPOAT():
    query = """
        select t.movie_id, t.imdb_id
        from links t 
        inner join (select movie_id , weighted_rating from movies 
        order by weighted_rating 
        desc limit 50) 
        m on m.movie_id = t.movie_id
        limit 50
    """
    cur = cnx.cursor(dictionary=True, buffered= True)
    cur.execute(query)
    mpoat = cur.fetchall()
    cur.close()
    return mpoat # will return none if nothing




