from fastapi import APIRouter

from app.schemas.auth_schema import (
    RegisterSchema,
    LoginSchema
)

from app.controllers.auth_controller import (
    register_controller,
    login_controller
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def register(
    data: RegisterSchema
):
    return register_controller(data)

@router.post("/login")
def login(
    data: LoginSchema
):
    return login_controller(data)