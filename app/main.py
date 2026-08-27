from fastapi import FastAPI
from app.routers.departmets_route import department
from app.routers.autentication_route import auth_route

app = FastAPI(
     title="Gestión de departamentos API",
    description="API para la gestion de departamentos integrando FastAPI y Supabase",
    version="1.0.0"
)

app.include_router(department)
app.include_router(auth_route)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API corriendo correctamente"}