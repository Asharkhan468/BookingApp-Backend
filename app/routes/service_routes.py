from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form


from app.schemas.service_schema import (
    ServiceSchema
)

from app.controllers.service_controller import create_service_controller


router = APIRouter(
    prefix="/services",
    tags=["Services"]
)

@router.post("/")
async def create_service(
    title: str = Form(...),
    description: str = Form(...),
    duration: str = Form(...),
    image: UploadFile = File(...)
):
    return await create_service_controller(
        title,
        description,
        duration,
        image
    )
@router.get("/")
def get_services():
    return get_services_controller()

@router.put("/{service_id}")
def update_service(
    service_id: str,
    data: ServiceSchema
):
    return update_service_controller(
        service_id,
        data
    )

@router.delete("/{service_id}")
def delete_service(
    service_id: str
):
    return delete_service_controller(
        service_id
    )