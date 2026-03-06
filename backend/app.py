from fastapi import FastAPI
import os
from dotenv import load_dotenv
from backend.routers.auth import auth_user
from backend.routers.movies import movies_router
load_dotenv()

app = FastAPI() #fastapi Initialization

#Including all Routes
app.include_router(auth_user, prefix = '/auth') #/auth/...
app.include_router(movies_router, prefix='/movies') #/movies/...
