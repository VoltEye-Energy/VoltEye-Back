
from fastapi import APIRouter
from websockets import route

from src.services.devices_service import DevicesService


router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)

@router.get("/{device_id}", summary="Pega informações do dispositivo")
async def get_device_info(device_id: str):
    service = DevicesService()
    device = service.get_device_by_id(device_id)    
    if not device:
        return {"status": "dispositivo não encontrado"} 
    return {
        "status": "sucesso",
        "device_key": device.device_key,
        "created_at": device.created_at,
    }