from app.database.connection import db

services_collection = db["services"]

class ServiceModel:

    @staticmethod
    def create_service(data):
        return services_collection.insert_one(data)

    @staticmethod
    def get_services():
        return list(services_collection.find())

    @staticmethod
    def get_service_by_id(service_id):
        from bson import ObjectId
        return services_collection.find_one({
            "_id": ObjectId(service_id)
        })

    @staticmethod
    def update_service(service_id, data):
        from bson import ObjectId

        return services_collection.update_one(
            {"_id": ObjectId(service_id)},
            {"$set": data}
        )

    @staticmethod
    def delete_service(service_id):
        from bson import ObjectId

        return services_collection.delete_one({
            "_id": ObjectId(service_id)
        })