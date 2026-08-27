from fastapi import APIRouter, Depends, HTTPException
from supabase import Client

from app.database.supabase import get_supabase
from app.dependencies.auth import get_current_user
from app.modules.apartments.repository import ApartmentRepository
from app.modules.apartments.service import ApartmentService

router = APIRouter(prefix="/departments", tags=["Departments"])

# Inyección del Servicio para mantener las rutas limpias
def get_department_service(db: Client = Depends(get_supabase)) -> ApartmentService:
    repo = ApartmentRepository(db)
    return ApartmentService(repo)

@router.get("/")
def get_all_departments(service: ApartmentService = Depends(get_department_service)):
    return service.list_departments()


# @department.get("/departments")
# def get(db: Client = Depends(get_supabase), current_user: dict= Depends(get_current_user)):
#     response = (
#         db.table("apartments")
#         .select("*")
#         .eq("user_id", "83aa1d02-dc30-4610-a759-fa62bac67850")
#         .execute()
        
#     )
#     print(response)
#     email = current_user.get("email")
#     print(email)
#     return response.data

# @department.get("/departments/{id}")
# def get_by_id(id, db: Client = Depends(get_supabase)):
#     try:
#         response = (
#             db.table("apartments")
#             .select("*")
#             .eq("id", id)
#             .execute()
#         )

#         # Validamos si la lista está vacía
#         if not response.data:
#             raise HTTPException(status_code=404, detail="Item no encontrado")
        
#         print(response)
#         return response.data[0]
#     except HTTPException:
#         raise
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))