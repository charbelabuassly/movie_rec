from datetime import datetime, timedelta, timezone
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
import os
from dotenv import load_dotenv
#We will start by creating the o2 scheme, this will extract the token from the authorization header incoming from the frontend
#through the http request
#the main idea is that when fastapi receieves the http request, it checks the auth header in the http header, Authorizaton : Bearer --jwt token--
#This function will extract the token as a string 

o2_scheme = OAuth2PasswordBearer(tokenUrl= 'token')
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

#The first function we need is the token creator function
def create_token(data : dict, expire_time : int):
    payload = data.copy()
    #We will pass a fixed 1 hour expire time from our current time
    expiry_time = datetime.now(timezone.utc) + timedelta(hours = expire_time) #timezone.utc will be used to negate timezone issues
    payload['exp'] = expiry_time
    #The expiry time has been set, now we need to build the jwt
    user_jwt = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)
    return user_jwt 

#Returns the user email and checks for any invalid token
def get_user(token : str = Depends(o2_scheme)):
    #We need to decode it, and validate the token
    try:
        payload = jwt.decode(token, key = SECRET_KEY, algorithms=[ALGORITHM])
        return payload['email']
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Expired Token")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail= "Unauthorized Access")
    
    
