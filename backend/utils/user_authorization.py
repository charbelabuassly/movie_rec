from fastapi import Depends, HTTPException
from backend.utils.jwt_handler import get_user
from backend.models.users_model import get_user_by_email


def require_user_by_email(email: str) -> dict:
    user = get_user_by_email(email)
    if user is None:
        raise HTTPException(status_code=404, detail="Account Not Found")
    return user


def get_current_user(email: str = Depends(get_user)) -> dict:
    return require_user_by_email(email)
