from src.bd.connect import connect
from src.schemas.medicao_schema import Medicao


class MedicaoRepository:
    table_name = "test_readings"

    def __init__(self):
        self.supabase = connect()

    def create(self, medicao: Medicao):
        return (
            self.supabase.table(self.table_name)
            .insert(medicao.model_dump(mode="json"))
            .execute()
        )
    def get_by_dispositivo_id(self, dispositivo_id: str):
        return (
            self.supabase.table(self.table_name)
            .select("*")
            .eq("dispositivo_id", dispositivo_id)
            .execute()
        )
