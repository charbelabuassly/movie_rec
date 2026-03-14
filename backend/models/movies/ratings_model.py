from backend.database.database import cnx 
from datetime import datetime 
#This will contain database querying that serves the ratings side

def insert_rating(movieId:int, rating:float, userId:int):
    insert_query = """
        insert into ratings (movie_id, user_id, rating, time_entered) values (%s, %s, %s, %s)
    """
    cur = cnx.cursor(dictionary=True, buffered= True)
    cur.execute(insert_query,(movieId,userId,rating,datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    cnx.commit()
    cur.close()
    
