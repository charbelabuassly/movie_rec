from backend.database.database import cnx 
from datetime import datetime 
#This will contain database querying that serves the ratings side

def insert_tag(movieId:int, tag:str, userId:int):
    insert_query = """
        insert into tags (movie_id, user_id, tag, time_entered) values (%s, %s, %s, %s)
    """
    cur = cnx.cursor(dictionary=True, buffered= True)
    cur.execute(insert_query,(movieId,userId,tag,datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    cnx.commit()
    cur.close()
    
