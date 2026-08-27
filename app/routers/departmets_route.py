from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from supabase import Client, create_client

from app.database import supabase
from app.database.supabase import get_supabase
from app.dependencies.auth import get_current_user

department = APIRouter()

@department.get("/departments")
def hello(db: Client = Depends(get_supabase), current_user: dict= Depends(get_current_user)):
    response = (
        db.table("apartments")
        .select("*")
        .eq("user_id", "83aa1d02-dc30-4610-a759-fa62bac67850")
        .execute()
        
    )
    print(response)
    email = current_user.get("email")
    print(email)
    return response.data

@department.get("/departments/{id}")
def get_by_id(id, db: Client = Depends(get_supabase)):
    try:
        response = (
            db.table("apartments")
            .select("*")
            .eq("id", id)
            .execute()
        )

        # Validamos si la lista está vacía
        if not response.data:
            raise HTTPException(status_code=404, detail="Item no encontrado")
        
        print(response)
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))