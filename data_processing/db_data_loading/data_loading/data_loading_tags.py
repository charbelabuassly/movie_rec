import numpy as np
import pandas as pd
import mysql.connector
import unicodedata 

def buildTags(cur,cnx):
    cur.execute('truncate table tags')
    df_tags = pd.read_csv('../datasets/cleaned_datasets/tags_cleaned.csv')
    df_tags['tag'] = df_tags['tag'].map(lambda x: unicodedata.normalize('NFC', str(x))) #fixing the duplicate issue in the db.
    df_tags = df_tags.drop_duplicates(subset=['movieId', 'userId', 'tag'], keep='first')
    i = 0
    for index, row in df_tags.iterrows():
        i+=1
        query = 'insert ignore into tags values (%s, %s, %s, %s)'
        cur.execute(query, (row.movieId, row.userId, row.tag, row.timestamp))
        if i == 10000:
            print("10000 inserted rows")
            i = 0
    cnx.commit()