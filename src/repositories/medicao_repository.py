from datetime import date

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
    
    def get_consumed_total(self, dispositivo_id: str):
        return (
            self.supabase.table(self.table_name)
            .select("*")
            .eq("device_key", dispositivo_id)
            .limit(10)
            .execute()
        )
    
    def get_consumed_by_dates(self, dispositivo_id: str, dateFrom: str, dateTo: str = None):
        if dateTo is None:
            dateTo = date.today().isoformat()

        return (
            self.supabase.table(self.table_name)
            .select("*")
            .eq("device_key", dispositivo_id)
            .gte("date", dateFrom)
            .lte("date", dateTo)
            .execute()
        )
    
    def get_consumed_by_day(self, dispositivo_id: str, date: str):
        return (
            self.supabase.table(self.table_name)
            .select("*")
            .eq("device_key", dispositivo_id)
            .eq("date", date)
            .execute()
        )
    
    def get_consumed_by_month(self, dispositivo_id: str, month: int, year: int):
        return (
            self.supabase.table(self.table_name)
            .select("*")
            .eq("device_key", dispositivo_id)
            .eq("month", month)
            .eq("year", year)
            .execute()
        )
    
    def get_consumed_by_year(self, dispositivo_id: str, year: int):
        return (
            self.supabase.table(self.table_name)
            .select("*")
            .eq("device_key", dispositivo_id)
            .eq("year", year)
            .execute()
        )
    
