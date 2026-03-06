import mysql.connector

def connect_db():
    return (
        mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database = 'movierecodb',
        allow_local_infile=True)
    )