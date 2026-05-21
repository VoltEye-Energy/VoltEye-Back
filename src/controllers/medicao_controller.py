from fastapi import APIRouter, HTTPException, status

from src.schemas.medicao_schema import Medicao, MedicaoResponse
from src.services.medicao_service import MedicaoService

router = APIRouter(
    prefix="/dispositivos",
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
async def receber_medicao(dispositivo_id: str, medicao: Medicao):
    service = MedicaoService()

    try:
        data = service.registrar_medicao(medicao)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao registrar medicao.",
        ) from exc

    return MedicaoResponse(
        status="sucesso",
        dispositivo_id=dispositivo_id,
        data=data,
    )


@router.get(
    "/{dispositivo_id}/medicoes",
    response_model=MedicaoResponse,
    status_code=status.HTTP_200_OK,
    summary="Pega dados de consumo eletrico",
    description="Endpoint responsavel por pegar medicoes enviadas por dispositivos.",
    responses={
        200: {"description": "Medicao encontrada com sucesso"},
        500: {"description": "Erro ao buscar medicao"},
    },
)
async def buscar_medicao(dispositivo_id: str, medicao: Medicao):
    service = MedicaoService()

    try:
        data = service.buscar_medicao(medicao)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao buscar medicao.",
        ) from exc

    return MedicaoResponse(
        status="sucesso",
        dispositivo_id=dispositivo_id,
        data=data,
    )


