from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router
from app.routes.service_routes import (
    router as service_router
)


app = FastAPI()

app.include_router(service_router)
app.include_router(auth_router)