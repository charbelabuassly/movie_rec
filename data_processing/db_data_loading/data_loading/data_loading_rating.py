import pandas as pd
import mysql.connector
from data_processing.db_data_loading.connector.connect_db import connect_db
import os
import time

def buildRatings(cur,cnx):
    cur.execute('truncate table ratings')
    start_time = time.time()
    #cur.execute("TRUNCATE TABLE ratings")  
    #print("Table cleared instantly")

    temp_file = os.path.abspath('../datasets/temp_ratings.csv')
    temp_file = temp_file.replace('\\', '/')

    df_ratings = pd.read_csv('../datasets/cleaned_datasets/ratings_cleaned.csv')
    df_ratings[['movieId', 'userId', 'rating', 'timestamp']].to_csv(
        temp_file, 
        index=False, 
        header=False
    )

    cur.execute("SET autocommit=0")
    cur.execute("SET unique_checks=0")
    cur.execute("SET foreign_key_checks=0")

    cur.execute(f"""
        LOAD DATA LOCAL INFILE '{temp_file}'
        INTO TABLE ratings
        FIELDS TERMINATED BY ','
        LINES TERMINATED BY '\\n'
        (movie_id, user_id, rating, time_entered)
    """)

    cur.execute("COMMIT")
    cur.execute("SET unique_checks=1")
    cur.execute("SET foreign_key_checks=1")

    if os.path.exists(temp_file):
        os.remove(temp_file)