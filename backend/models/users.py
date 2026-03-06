from backend.database.database import cnx  
from mysql.connector.errors import Error
#This will contain database querying that serves the user side

def get_user_by_email(email) -> dict:
    cur = cnx.cursor(dictionary=True, buffered=True)
    cur.execute("Select * from users where user_email = (%s)", (email,))
    user = cur.fetchone()
    cur.close() #closing to prevent memory leak
    return user  
    
def register_user(data : dict):
    cur = cnx.cursor(dictionary=True, buffered=True)
    cur.execute("Select max(user_id) as max_id from users")
    new_max = (cur.fetchone())['max_id']
    if new_max is None: #Just in case, the loaded users table is clean from data
        new_max = 0 
    new_max+=1
    insert_query = """
        INSERT INTO users (user_id, user_name, user_email, user_password, is_deleted)
        VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(insert_query,(new_max, data['name'], data['email'], data['password'], 0))
    cnx.commit()
    cur.close()
