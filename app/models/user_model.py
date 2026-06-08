from app.database.connection import users_collection

class UserModel:

    @staticmethod
    def create_user(data):
        return users_collection.insert_one(data)

    @staticmethod
    def find_by_email(email):
        return users_collection.find_one(
            {"email": email}
        )