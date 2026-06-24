from fastapi import APIRouter, HTTPException
from src.services.devices_service import DevicesService
from src.services.medicao_service import MedicaoService
from src.schemas.devices_schema import DeviceChartResponse, DeviceStatusResponse, DeviceInsightsResponse, DeviceTariffRequest, DeviceTariffResponse

from datetime import datetime, timedelta, timezone


router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
)


@router.get("", summary="Pega informações de todos os dispositivos")
async def listar_dispositivos():
    service = DevicesService()

    try:
        devices = service.get_all_devices()
        print(devices)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Erro ao buscar dispositivos."
        ) from exc

    return {"data": devices}


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


@router.get(
    "/{device_id}/chart",
    response_model=DeviceChartResponse,
    summary="Retorna dados para gráficos",
    description="Retorna leituras formatadas para gráficos de consumo."
)
async def get_chart(device_id: str):
    medicao_service = MedicaoService()
    device_service = DevicesService()

    if not device_service.get_device_by_id(device_id):
        raise HTTPException(404, "Dispositivo não encontrado")

    points = medicao_service.buscar_dados_grafico(device_id)

    return DeviceChartResponse(
        device_id=device_id,
        points=points
    )


@router.get(
    "/{device_id}/status",
    response_model=DeviceStatusResponse,
    summary="Retorna status da tomada",
    description="Verifica se a tomada está online com base na última telemetria."
)
async def get_status(device_id: str):
    medicao_service = MedicaoService()
    device_service = DevicesService()

    if not device_service.get_device_by_id(device_id):
        raise HTTPException(404, "Dispositivo não encontrado")

    last_seen = medicao_service.buscar_ultima_medicao(device_id)

    online = False

    if last_seen:
        if isinstance(last_seen, str):
            last_seen = datetime.fromisoformat(
                last_seen.replace("Z", "+00:00")
            )

        online = (datetime.now(timezone.utc) - last_seen) < timedelta(minutes=5)

    return DeviceStatusResponse(
        device_id=device_id,
        status="online" if online else "offline",
        last_seen=str(last_seen) if last_seen else None
    )

@router.get(
    "/{device_id}/insights",
    response_model=DeviceInsightsResponse,
    summary="Retorna insights de consumo",
    description="Gera insights simples baseados nas leituras."
)
async def get_insights(device_id: str):
    medicao_service = MedicaoService()
    device_service = DevicesService()

    if not device_service.get_device_by_id(device_id):
        raise HTTPException(404, "Dispositivo não encontrado")

    insights = medicao_service.gerar_insights(device_id)

    return DeviceInsightsResponse(
        device_id=device_id,
        insights=insights
    )


@router.put(
    "/{device_id}/tariff",
    response_model=DeviceTariffResponse,
    summary="Configura valor do kWh",
    description="Atualiza a tarifa de energia usada para cálculo de custos."
)
async def update_tariff(
    device_id: str,
    payload: DeviceTariffRequest
):
    service = DevicesService()

    if not service.get_device_by_id(device_id):
        raise HTTPException(404, "Dispositivo não encontrado")

    service.atualizar_tarifa(device_id, payload.tariff)

    return DeviceTariffResponse(
        device_id=device_id,
        tariff=payload.tariff,
        message="Tarifa atualizada com sucesso"
    )
