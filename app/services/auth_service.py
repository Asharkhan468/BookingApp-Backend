from app.models.user_model import UserModel
from app.utils.password import (
    hash_password,
    verify_password
)
from app.utils.jwt import create_access_token

class AuthService:

    @staticmethod
    def register(data):

        existing_user = UserModel.find_by_email(
            data.email
        )

        if existing_user:
            raise Exception(
                "Email already exists"
            )

        user = {
            "name": data.name,
            "email": data.email,
            "phone": data.phone,
            "password": hash_password(
                data.password
            )
        }

        UserModel.create_user(user)

        return {
            "message":
            "User registered successfully"
        }

    @staticmethod
    def login(data):

        user = UserModel.find_by_email(data.email)

        if not user:
            raise Exception("Invalid credentials")

        if not verify_password(
            data.password,
            user["password"]
        ):
            raise Exception("Invalid credentials")

        token = create_access_token({
            "user_id": str(user["_id"]),
            "email": user["email"]
        })

        return {
            "message": "Login successful",
            "token": token,
            "user": {
                "id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"],
                "phone": user["phone"]
            }
        }