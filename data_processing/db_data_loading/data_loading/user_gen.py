import random
import bcrypt
from password_generator import PasswordGenerator

first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Sophia', 'Mason', 'Isabella', 'William',
               'Mia', 'James', 'Charlotte', 'Benjamin', 'Amelia', 'Lucas', 'Harper', 'Henry', 'Evelyn', 'Alexander',
               'Abigail', 'Michael', 'Emily', 'Daniel', 'Elizabeth', 'Matthew', 'Sofia', 'Jackson', 'Avery', 'David']

last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
              'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin',
              'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson']

domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com']

BCRYPT_ROUNDS = 4  

def gen_user(user_id):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    domain = random.choice(domains)
    email = f'{fname}{lname}{user_id}@{domain}'

    password = "Password123!" 

    hashed_password = bcrypt.hashpw(
        password[:72].encode('utf-8'), 
        bcrypt.gensalt(rounds=BCRYPT_ROUNDS)
    ).decode('utf-8')

    return fname, email, hashed_password