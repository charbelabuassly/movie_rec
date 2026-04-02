# --------------
# MORE LIKE THIS 
# --------------

"""
In this section, most similar movies to the one selected will be returned
"""


from backend.database.database import cnx

def getmlt(movie_id):
    query = """
    select * from movie_similarity where movie_id = (%s) order by ranking
    """
    cur = cnx.cursor(dictionary=True, buffered= True)
    cur.execute(query,(movie_id,))
    mpoat = cur.fetchall()
    cur.close()
    return mpoat # will return none if nothing