from fastapi import APIRouter, HTTPException, status

from services.user_service import UserService
from src.schemas.user_schema import UserResponse, userCreate
router = APIRouter(
    prefix="/",
    tags=["Users"],
)


@router.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Recebe dados para criar usuário",
    description="Endpoint responsavel por receber dados de criação de usuário.",
    responses={
        201: {"description": "Usuário criado com sucesso"},
        500: {"description": "Erro ao criar usuário"},
    },
)
async def create_user(user_data: userCreate):
    service = UserService()

    try:
        data = service.create_user(user_data)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao criar usuário.",
        ) from exc

    return UserResponse(
        status="sucesso",
        id=data.id,
        name=data.name,
        email=data.email
    )



