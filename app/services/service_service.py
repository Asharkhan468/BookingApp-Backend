from app.models.service_model import ServiceModel
from app.utils.cloudinary import upload_image

class ServiceService:

    @staticmethod
    async def create(
        title,
        description,
        duration,
        image
    ):

        image_url = upload_image(image)

        service = {
            "title": title,
            "description": description,
            "duration": duration,
            "imageUrl": image_url
        }

        result = ServiceModel.create_service(
            service
        )

        return {
    "message": "Service created successfully",
    "serviceId": str(
        result.inserted_id
    ),
    "imageUrl": image_url
}

    @staticmethod
    def get_all():
        services = ServiceModel.get_services()

        formatted = []

        for service in services:
            formatted.append({
                "id": str(service["_id"]),
                "title": service["title"],
                "description": service["description"],
                "duration": service["duration"],
                "imageUrl": service["imageUrl"]
            })

            return formatted

    @staticmethod
    def update(service_id, data):

        ServiceModel.update_service(
            service_id,
            data.model_dump()
        )

        return {
    "message": "Service updated successfully"
}

    @staticmethod
    def delete(service_id):

        ServiceModel.delete_service(service_id)

        return {
    "message": "Service deleted successfully"
}