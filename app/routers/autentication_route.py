


from fastapi import APIRouter, Depends, HTTPException
from supabase import Client

from app.database.supabase import get_supabase
from app.dependencies.auth import get_current_user
from app.schemas.user_credentials import UserCredentials


auth_route = APIRouter()


# LOGIN
@auth_route.post("/auth/login", summary= "Iniciar Sesión")
def login(credentials: UserCredentials, db: Client = Depends(get_supabase)):
    try:
        response = db.auth.sign_in_with_password(
            {
                "email": credentials.email,
                "password": credentials.password
            }
        )

        #retorna el access_token
        return {
            "access_token": response.session.access_token,
            "token_type": "bearer"
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="Credenciales invalidas")


#GET USER INFO CURRENT
@auth_route.get("/auth/me", summary="Obtener información del usuario actual")
def get_me(current_user: dict = Depends(get_current_user)):
    return{
        "user_id": current_user.get("sub"),
        "email": current_user.get("email"),
        "role": current_user.get("role")
    }