from fastapi import FastAPI
from backend.routers.auth_route import auth_user
from backend.routers.movies_route import movies_router
from backend.routers.recommendation_route import recommendation_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() #fastapi Initialization
origins = [
    "http://localhost:5173" 
]

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Including all Routes (Exception occurs when invalid user input/internal errors)
app.include_router(auth_user, prefix = '/auth') #/auth/...
app.include_router(movies_router, prefix='/movies') #/movies/...
app.include_router(recommendation_router, prefix='/recommendations') #/recommendations/...

