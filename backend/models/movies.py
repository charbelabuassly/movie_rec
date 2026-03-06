from backend.database.database import cnx  
#This will contain database querying that serves the movies side

#For example Add/Remove movies from the watch-list

def checkMovie(movieId : int) -> bool:
    cur = cnx.cursor(dictionary=True, buffered=True)
    #The first step to prevent entering garbage data into the system, is to check whether the movie exists or not
    select_query = """
        select movie_id from movies where movie_id = (%s)
    """
    cur.execute(select_query,(movieId,))
    movie_status = cur.fetchone()['movie_id']
    cur.close()
    if movie_status is None:
        return False
    else:
        return True
    
    

def addMovie(movieId : int, userId : int):
    insert_query = """
        Insert into watch_list (movie_id, user_id, watched, is_deleted) values (%s, %s ,%s ,%s)
    """
    cur = cnx.cursor(dictionary=True, buffered=True)
    cur.execute(insert_query, (movieId, userId, 0, 0))
    cnx.commit()
    cur.close()
    
def removeMovie(movieId : int, userId : int): # TO MODIFY => Make sure it adds the ratings and tags if they exist. 
    update_query = """
        update watch_list set is_deleted = 1 where user_id = (%s) and movie_id = (%s)
    """
    cur = cnx.cursor(dictionary=True, buffered=True)
    cur.execute(update_query, (userId, movieId))
    cnx.commit()
    cur.close()
    
def setWatched(movieId : int, userId : int):
    update_query = """
        update watch_list set watched = 1 where user_id = (%s) and movie_id = (%s)
    """
    cur = cnx.cursor(dictionary=True, buffered=True)
    cur.execute(update_query, (userId, movieId))
    cnx.commit()
    cur.close()
    