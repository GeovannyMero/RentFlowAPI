
from fastapi import FastAPI


app = FastAPI(
     title="Gestión de departamentos API",
    description="API para la gestion de departamentos integrando FastAPI y Supabase",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Hola"}