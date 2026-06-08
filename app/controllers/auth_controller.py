from fastapi import HTTPException
from app.services.auth_service import AuthService

def register_controller(data):
    try:
        return AuthService.register(data)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

def login_controller(data):
    try:
        return AuthService.login(data)

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )