from typing import Any

from src.repositories.medicao_repository import MedicaoRepository
from src.schemas.medicao_schema import Medicao


class MedicaoService:
    def __init__(self):
        self.repository = MedicaoRepository()

    def registrar_medicao(self, medicao: Medicao) -> list[dict[str, Any]] | None:
        response = self.repository.create(medicao)
        return response.data
    
    def buscar_medicao(self, medicao: Medicao) -> list[dict[str, Any]] | None:
        response = self.repository.get_by_dispositivo_id(medicao.dispositivo_id)
        return response.data
    
    def buscar_consumo_total(self, dispositivo_id: str) -> list[dict[str, Any]] | None:
        response = self.repository.get_consumed_total(dispositivo_id)
        return response.data
    
    def buscar_consumo_por_datas(self, dispositivo_id: str, dateFrom: str, dateTo: str = None) -> list[dict[str, Any]] | None:
        response = self.repository.get_consumed_by_dates(dispositivo_id, dateFrom, dateTo)
        return response.data
    
    def buscar_consumo_por_dia(self, dispositivo_id: str, date: str) -> list[dict[str, Any]] | None:
        response = self.repository.get_consumed_by_day(dispositivo_id, date)
        return response.data
    
    def buscar_consumo_por_mes(self, dispositivo_id: str, month: int, year: int) -> list[dict[str, Any]] | None:
        response = self.repository.get_consumed_by_month(dispositivo_id, month, year)
        return response.data
    
    def buscar_consumo_por_ano(self, dispositivo_id: str, year: int) -> list[dict[str, Any]] | None:
        response = self.repository.get_consumed_by_year(dispositivo_id, year)
        return response.data
    
