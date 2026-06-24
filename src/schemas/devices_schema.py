from supabase_auth import BaseModel, Optional, datetime
from typing import List


class Device(BaseModel):
    id: str
    device_key: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DeviceStatusResponse(BaseModel):
    device_id: str
    status: str
    last_seen: str | None = None


class ChartPoint(BaseModel):
    label: str
    value: float


class DeviceChartResponse(BaseModel):
    device_id: str
    points: List[ChartPoint]


class Insight(BaseModel):
    message: str


class DeviceInsightsResponse(BaseModel):
    device_id: str
    insights: List[Insight]


class DeviceTariffResponse(BaseModel):
    device_id: str
    tariff: float
    message: str

class DeviceTariffRequest(BaseModel):
    tariff: float
