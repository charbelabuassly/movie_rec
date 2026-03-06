import numpy as np
import pandas as pd
import mysql.connector
from data_processing.db_data_loading.connector.connect_db import connect_db
#Connecting to the server
def buildGenres(cur,cnx):
    cur.execute('delete from genres')
    genre_set = set()
    df_movies = pd.read_csv('../datasets/cleaned_datasets/movies_cleaned.csv')
    for index,row in df_movies.iterrows():
        genre_list = row.genres.strip().split('|')
        for genre in genre_list:
            genre_set.add(genre)
    print(genre_set)
    for genre in genre_set:
        query = 'insert into genres (genre) values (%s)'
        cur.execute(query, (genre,))
        
    cnx.commit()


