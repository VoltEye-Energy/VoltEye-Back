from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class Medicao(BaseModel):
    corrente: float = Field(..., examples=[2.5])
    tensao: float = Field(..., examples=[220])
    potencia: float = Field(..., examples=[550])
    device_key: str = Field(..., examples=["abc123"])
    timestamp: datetime | None = Field(default=None, examples=["2026-04-25T14:30:00Z"])


class MedicaoResponse(BaseModel):
    status: str
    device_key: str
    data: list[dict[str, Any]] | None = None
