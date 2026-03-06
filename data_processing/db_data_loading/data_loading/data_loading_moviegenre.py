import numpy as np
import pandas as pd
import mysql.connector
from data_processing.db_data_loading.connector.connect_db import connect_db

def buildMovieGenre(cur,cnx):
    cur.execute('truncate table movie_genre')
    df_movies = pd.read_csv('../datasets/cleaned_datasets/movies_cleaned.csv')
    i = 0 
    for index, row in df_movies.iterrows():
        i+=1
        genre_list = row['genres'].split('|')
        for genre in genre_list:
            cur.execute('select genre_id from genres where genre = %s', (genre.strip(),))
            #print(genre.strip())
            result = cur.fetchone()[0] #returns a tuple 
            cur.execute('insert into movie_genre (movie_id , genre_id) values (%s,%s)', (row['movieId'],result))
            #print("insertion success")
        if i == 10000:
            print("10000 inserts")
            i = 0
    cnx.commit()
