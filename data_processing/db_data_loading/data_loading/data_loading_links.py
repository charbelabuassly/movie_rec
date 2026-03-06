import numpy as np
import pandas as pd
import mysql.connector
from data_processing.db_data_loading.connector.connect_db import connect_db
#Connecting to the server

def buildLinks(cur,cnx):
    cur.execute('truncate table links')
    df_tags = pd.read_csv('../datasets/cleaned_datasets/links_cleaned.csv')
    i = 0
    for index, row in df_tags.iterrows():
        i+=1
        query = 'insert into links values (%s, %s, %s)'
        cur.execute(query, (row.movieId, row.imdbId, row.tmdbId))
        if i == 10000:
            print("10000 inserted rows")
            i = 0
    cnx.commit()