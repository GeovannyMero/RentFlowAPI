from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt import PyJWKClient
from supabase import Client

from app.database.supabase import get_supabase

security = HTTPBearer()

# Reemplaza con la URL de tu proyecto Supabase
SUPABASE_URL = "https://ocuthcfnwaftvawdxgcy.supabase.co"
JWKS_URL = f"{SUPABASE_URL}/auth/v1/.well-known/jwks.json"

# Inicializa el cliente JWKS para obtener y cachear las llaves públicas
jwks_client = PyJWKClient(JWKS_URL)

SUPABASE_JWT_SECRET = "legyWprupAnr+pR7KX3KW5ThdFDof+r4FPwGHzQJ+PBGtted/p/gG5LMJ0xDqg214ATVmV5xs8Ulz2BaXjQomA=="

def get_current_user(
        creadentials: HTTPAuthorizationCredentials = Depends(security), 
        db: Client = Depends(get_supabase)
    ):
    token = creadentials.credentials
    print(token)
    try:
        # Obtiene automáticamente la clave pública correspondiente al 'kid' del token
        signing_key = jwks_client.get_signing_key_from_jwt(token)

        payload = jwt.decode(
            token,
            signing_key.key,
            algorithms=["ES256"],
            options={"verify_aud":False}
            
        )
        return payload
    except jwt.PyJWTError as e:
        print("Error en JWT:", str(e))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    