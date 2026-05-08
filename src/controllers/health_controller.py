from fastapi import APIRouter

router = APIRouter(tags=["Status"])


@router.get("/", summary="Verifica se a API esta online")
def read_root():
    return {"message": "VoltEye API"}
