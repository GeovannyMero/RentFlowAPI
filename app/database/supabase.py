from supabase import Client, create_client
from app.core.config import Settings

settings = Settings()

def get_supabase() -> Client:
    client: Client = create_client(settings.supabase_url, settings.supabase_key)

    try:
        yield client
    finally:
        pass