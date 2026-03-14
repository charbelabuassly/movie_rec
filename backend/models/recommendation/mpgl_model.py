# -------------------------
# MOST POPULAR GENRE LIST
# -------------------------

"""
In this section, we will return the top 3 most popular genres from the database. It will be based on 2 criteria:
    1- highest average rating
    2- highest movie counts 
"""

from backend.database.database import cnx

def getPopularGenres():
    query = """
    select mg.genre_id, avg(m.weighted_rating) as avg_rating, g.genre  from
    movie_genre mg 
    inner join movies m on m.movie_id = mg.movie_id
    inner join genres g on g.genre_id = mg.genre_id
    group by mg.genre_id
    order by avg_rating DESC
    """
    cur = cnx.cursor(dictionary=True, buffered= True)
    cur.execute(query)
    mpoat = cur.fetchall()
    return mpoat # will return none if nothing
