from fastapi import FastAPI
from app.routers.departmets_route import department

app = FastAPI(
     title="Gestión de departamentos API",
    description="API para la gestion de departamentos integrando FastAPI y Supabase",
    version="1.0.0"
)

app.include_router(department)

# @app.get("/")
# def home():
#     return {"message": "Hola"}