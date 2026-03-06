import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
#from data_processing.db_data_loading.connector.connect_db import connect_db

def buildSimilarityTable(cur,cnx,batch_size=5000):
    
    df_rating = pd.read_csv('../datasets/cleaned_datasets/ratings_cleaned.csv')
    df_movies = pd.read_csv('../datasets/cleaned_datasets/movies_cleaned.csv')

    df_merged = df_rating.merge(df_movies, on = 'movieId', how = 'inner')[['userId','movieId','rating']]
    pivot = df_merged.pivot_table(index = 'userId', columns = 'movieId', values = 'rating', aggfunc = 'mean') #we use this agg function because a user might've rated the same movie multiple times

    sparse = csr_matrix(pivot.fillna(0).values)

    similarity_matrix = cosine_similarity(sparse.T, dense_output=False) 

    idx_movieid_map = pd.Series(df_movies['movieId'].values)
    
    # Clear the table first
    cur.execute('TRUNCATE TABLE movie_similarity')
    
    insert_query = """
        INSERT INTO movie_similarity (movie_id, similar_movie_id, ranking, similarity_score)
        VALUES (%s, %s, %s, %s)
    """
    
    batch = []  
    
    for idx in range(similarity_matrix.shape[0]):
        # get the similarity row as 1D array
        movie_similarity = similarity_matrix.getrow(idx).toarray().flatten()
        movie_similarity[idx] = -1  
        
        # top 20 similar movies
        most_similar_indices = movie_similarity.argsort()[::-1][:20]
        
        movie_id = int(idx_movieid_map.iloc[idx])  # actual movie id
        
        rank = 1
        for i in most_similar_indices:
            similar_movie_id = int(idx_movieid_map.iloc[i])
            similarity_score = float(movie_similarity[i])
            batch.append((movie_id, similar_movie_id, rank, similarity_score))
            rank += 1
        
        # Insert batch if it reaches batch_size
        if len(batch) >= batch_size:
            cur.executemany(insert_query, batch)
            cnx.commit()
            batch = []
    
    # insert any remaining rows
    if batch:
        cur.executemany(insert_query, batch)
        cnx.commit()
    
    
