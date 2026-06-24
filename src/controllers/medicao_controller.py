from fastapi import APIRouter, HTTPException, status

from src.schemas.medicao_schema import GetMedicaoResponse, Medicao, MedicaoResponse
from src.services.devices_service import DevicesService
from src.services.medicao_service import MedicaoService

router = APIRouter(
    prefix="/medicoes",
    tags=["Medicoes"],
)

@router.post(
    "/{dispositivo_id}/medicoes",
    response_model=MedicaoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Recebe dados de consumo eletrico",
    description="Endpoint responsavel por receber medicoes enviadas por dispositivos.",
    responses={
        201: {"description": "Medicao registrada com sucesso"},
        500: {"description": "Erro ao registrar medicao"},
    },
)
async def receber_medicao( medicao: Medicao):
    service = MedicaoService()
    device = DevicesService()

    if not device.get_device_by_id(medicao.device_key):
        device.create_device(medicao.device_key)

    try:
        data = service.registrar_medicao(medicao)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao registrar medicao.",
        ) from exc

    return MedicaoResponse(
        status="sucesso",
        device_key=medicao.device_key,
        data=data,
    )


@router.get(
    "/devices/{dispositivo_id}/current",
    response_model=GetMedicaoResponse,
    status_code=status.HTTP_200_OK,
    summary="Pega dados de consumo eletrico",
    description="Endpoint responsavel por pegar medicoes enviadas por dispositivos.",
    responses={
        200: {"description": "Medicao encontrada com sucesso"},
        500: {"description": "Erro ao buscar medicao"},
    },
)
async def buscar_consumo_atual(dispositivo_id: str):
    service = MedicaoService()
    device = DevicesService()

    if not device.get_device_by_id(dispositivo_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dispositivo não encontrado.",
        )
    try:
        data = service.buscar_consumo_total(dispositivo_id)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao buscar consumo total.",
        ) from exc

    return GetMedicaoResponse(data=data)

@router.get(
    "/devices/{dispositivo_id}/readings",
    response_model=GetMedicaoResponse,
    status_code=status.HTTP_200_OK,
    summary="Pega dados de consumo eletrico",
    description="Endpoint responsavel por pegar medicoes enviadas por dispositivos em um determinado período.",
    responses={
        200: {"description": "Medicao encontrada com sucesso"},
        500: {"description": "Erro ao buscar medicao"},
    },
)
async def buscar_consumo_por_datas(dispositivo_id: str, dateFrom: str, dateTo: str = None):
    service = MedicaoService()
    device = DevicesService()

    if not device.get_device_by_id(dispositivo_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dispositivo não encontrado.",
        )

    try:
        data = service.buscar_consumo_por_datas(dispositivo_id, dateFrom, dateTo)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao buscar consumo por datas.",
        ) from exc

    return GetMedicaoResponse(data=data)
    


@router.get(
    "/devices/{dispositivo_id}/summary/day",
    response_model=GetMedicaoResponse,
    status_code=status.HTTP_200_OK,
    summary="Pega dados de consumo eletrico",
    description="Endpoint responsavel por pegar resumos de consumo por dia.",
    responses={
        200: {"description": "Medicao encontrada com sucesso"},
        500: {"description": "Erro ao buscar medicao"},
    },
)
async def buscar_consumo_por_dia(dispositivo_id: str, date: str):
    service = MedicaoService()
    device = DevicesService()

    if not device.get_device_by_id(dispositivo_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dispositivo não encontrado.",
        )

    try:
        data = service.buscar_consumo_por_dia(dispositivo_id, date)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao buscar consumo por dia.",
        ) from exc

    return GetMedicaoResponse(data=data)


@router.get(
    "/devices/{dispositivo_id}/summary/month",
    response_model=GetMedicaoResponse,
    status_code=status.HTTP_200_OK,
    summary="Pega dados de consumo eletrico",
    description="Endpoint responsavel por pegar resumos de consumo por mes.",
    responses={
        200: {"description": "Medicao encontrada com sucesso"},
        500: {"description": "Erro ao buscar medicao"},
    },
)
async def buscar_consumo_por_mes(dispositivo_id: str, month: int, year: int):
    service = MedicaoService()
    device = DevicesService()  

    if not device.get_device_by_id(dispositivo_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dispositivo não encontrado.",
        )

    try:
        data = service.buscar_consumo_por_mes(dispositivo_id, month, year)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao buscar consumo por mes.",
        ) from exc

    return GetMedicaoResponse(data=data)


@router.get(
    "/devices/{dispositivo_id}/summary/year",
    response_model=GetMedicaoResponse,
    status_code=status.HTTP_200_OK,
    summary="Pega dados de consumo eletrico",
    description="Endpoint responsavel por pegar resumos de consumo por ano.",
    responses={
        200: {"description": "Medicao encontrada com sucesso"},
        500: {"description": "Erro ao buscar medicao"},
    },
)
async def buscar_consumo_por_ano(dispositivo_id: str, year: int):
    service = MedicaoService()
    device = DevicesService()

    if not device.get_device_by_id(dispositivo_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dispositivo não encontrado.",
        )

    try:
        data = service.buscar_consumo_por_ano(dispositivo_id, year)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao buscar consumo por ano.",
        ) from exc

    return GetMedicaoResponse(data=data)    
