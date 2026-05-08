from supabase import create_client, Client

from src.core.config import settings


def connect() -> Client:
    return create_client(settings.supabase_url, settings.supabase_key)
