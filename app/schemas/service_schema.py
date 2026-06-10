from pydantic import BaseModel

class ServiceSchema(BaseModel):
    title: str
    description: str
    duration: str
    imageUrl: str