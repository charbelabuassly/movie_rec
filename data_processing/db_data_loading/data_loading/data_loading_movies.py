import numpy as np
import pandas as pd
import mysql.connector
from data_processing.db_data_loading.connector.connect_db import connect_db
#Connecting to the server
def buildMovies(cur,cnx):
    cur.execute('delete from movies')
    df_movies = pd.read_csv('../datasets/cleaned_datasets/movies_cleaned.csv')
    #now we need to insert the movies into the movies table

    for index, row in df_movies.iterrows():
        cur.execute(
            "INSERT INTO movies (movie_id, title, weighted_rating) VALUES (%s, %s, %s)",
            (row.movieId, row.title, row.weighted_rating)
        )
    cnx.commit()