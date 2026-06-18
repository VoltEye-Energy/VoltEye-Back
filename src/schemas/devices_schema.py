

from supabase_auth import BaseModel, Optional, datetime


class Device(BaseModel):
    id: str
    device_key: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


