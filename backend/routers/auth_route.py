from backend.schemas.auth_schema import LoginRequest, SignupRequest
from backend.controllers.auth.users_controller import login_controller, signup_controller
from fastapi import APIRouter
#This page will handle all user related urls. Like Login , Login etc
    
    

auth_user = APIRouter()
@auth_user.post('/login')
async def login(request : LoginRequest):
    return login_controller(request)



@auth_user.post('/signup')
async def signup(request : SignupRequest):
    return signup_controller(request)
