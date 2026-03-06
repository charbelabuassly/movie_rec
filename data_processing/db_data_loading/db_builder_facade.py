import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from data_processing.db_data_loading.connector.connect_db import connect_db
from data_processing.db_data_loading.data_loading.data_loading_genres import buildGenres
from data_processing.db_data_loading.data_loading.data_loading_moviegenre import buildMovieGenre
from data_processing.db_data_loading.data_loading.data_loading_movies import buildMovies
from data_processing.db_data_loading.data_loading.data_loading_rating import buildRatings
from data_processing.db_data_loading.data_loading.data_loading_tags import buildTags
from data_processing.db_data_loading.data_loading.data_loading_users import buildUser
from data_processing.db_data_loading.data_loading.data_loading_links import buildLinks
from data_processing.db_data_loading.data_loading.data_movie_sim_load import buildSimilarityTable

def buildDB():
    cnx = connect_db()
    cur = cnx.cursor()
    cnx.commit()
    buildUser(cur,cnx)
    print("Users Table Built")
    buildMovies(cur,cnx)
    print("Movies Table Built")
    buildGenres(cur,cnx)
    print("Genres Table Built")
    buildLinks(cur,cnx)
    print("Links Table Built")
    buildTags(cur,cnx)
    print("Tags Table Built")
    buildRatings(cur,cnx)
    print("Ratings Table Built")
    buildMovieGenre(cur,cnx)
    print("Movie_Genre Table Built")
    buildSimilarityTable(cur,cnx)
    print("Movie Similarity Table Built")
    cur.close()
    cnx.close()
    
buildDB()