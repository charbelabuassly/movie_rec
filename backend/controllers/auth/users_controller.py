from fastapi import HTTPException
from backend.models.users.users_model import get_user_by_email, register_user
from backend.utils.pass_handler import verify_password, hash_password, validate_pass
from backend.utils.jwt_handler import create_token
import os
from dotenv import load_dotenv

load_dotenv()
EXPIRE_TIME = int(os.getenv('EXPIRE_TOKEN_TIME'))


def login_controller(request) -> dict: #We will return the token as {'access-token' : token}, this is if we need to return anything 
    #else in the future
    email : str = request.email
    password :str = request.password
    row = get_user_by_email(email)
    if row is None:
        raise HTTPException(status_code=401, detail="Invalid Credentials") #returning an error rather than response to 
        #axios.post request for the login in the frontend
    #else we do have a row, we need to verify the password
    stored_pass = row['user_password'].strip()
    #We need to verify the password
    if not(verify_password(password,stored_pass)):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    else:
        #we can create the token
        return {
            "status": True,
            "message": "Login successful",
            "data": {"access_token": create_token({"email": email}, EXPIRE_TIME)},
        }
        
        
        
        
def signup_controller(request) -> dict: #Will return jwt token upon account creation
    name = request.name
    #Before hashing the password , validate it
    if not validate_pass(request.password):
        raise HTTPException(status_code=400, detail="Invalid Password")
    else:
        password = hash_password(request.password)
        email = request.email
        row = get_user_by_email(email)
        if row is not None:
            raise HTTPException(status_code=400, detail="Account already exists")
        else:
            register_user({"name" : name, "password" : password, "email" : email})
            #Create the token
            return {
                "status": True,
                "message": "Signup successful",
                "data": {"access_token": create_token({"email": email}, EXPIRE_TIME)},
            }
        
