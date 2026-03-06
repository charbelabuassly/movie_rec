import numpy as np
import pandas as pd
from data_processing.db_data_loading.data_loading.user_gen import gen_user

def buildUser(cur, cnx):
    print("Deleting existing users...")
    while True:
        cur.execute("DELETE FROM users LIMIT 500")
        cnx.commit()
        if cur.rowcount == 0:
            break
        print(f"Deleted {cur.rowcount} users in this batch")

    print("Users table cleared.")

    df_tags = pd.read_csv('../datasets/cleaned_datasets/tags_cleaned.csv')
    df_ratings = pd.read_csv('../datasets/cleaned_datasets/ratings_cleaned.csv')

    u_id = pd.Series(np.concatenate([df_ratings['userId'].unique(), df_tags['userId'].unique()]))
    u_id = u_id.unique()
    total_users = len(u_id)
    print(f"Total unique users to insert: {total_users}")

    users_to_insert = []
    for idx, u in enumerate(u_id, 1):
        name, email, password = gen_user(u)
        users_to_insert.append((int(u), name, email, password, 0))
        if idx % 5000 == 0:
            print(f"Generated {idx}/{total_users} users")

    insert_query = """
        INSERT INTO users (user_id, user_name, user_email, user_password, is_deleted)
        VALUES (%s, %s, %s, %s, %s)
    """
    batch_size = 500
    for i in range(0, total_users, batch_size):
        batch = users_to_insert[i:i+batch_size]
        cur.executemany(insert_query, batch)
        cnx.commit()
        print(f"Inserted batch {i//batch_size + 1}: {len(batch)} users (Total inserted: {min(i+batch_size, total_users)}/{total_users})")

    print("All users inserted successfully.")