from fastapi import HTTPException
from app.services.service_service import ServiceService

async def create_service_controller(
    title,
    description,
    duration,
    image
):
    return await ServiceService.create(
        title,
        description,
        duration,
        image
    )
def get_services_controller():
    return ServiceService.get_all()

def update_service_controller(
    service_id,
    data
):
    return ServiceService.update(
        service_id,
        data
    )

def delete_service_controller(
    service_id
):
    return ServiceService.delete(
        service_id
    )