from fastapi import APIRouter, Depends
from supabase import Client

from app.database.supabase import get_supabase

department = APIRouter()

@department.get("/departments")
def hello(db: Client = Depends(get_supabase)):
    response = (
        db.table("apartments")
        .select("*")
        .execute()
    )
    return response.data