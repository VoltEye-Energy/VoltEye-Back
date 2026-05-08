from typing import Any

from src.repositories.medicao_repository import MedicaoRepository
from src.schemas.medicao_schema import Medicao


class MedicaoService:
    def __init__(self):
        self.repository = MedicaoRepository()

    def registrar_medicao(self, medicao: Medicao) -> list[dict[str, Any]] | None:
        response = self.repository.create(medicao)
        return response.data
