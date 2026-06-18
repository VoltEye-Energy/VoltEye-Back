from src.bd.connect import connect
from src.schemas.devices_schema import Device


class DevicesRepository:

    table_name = "teste_devices"

    def __init__(self):
        self.supabase = connect()

    def create_device(self, device: Device):
        return (
            self.supabase.table(self.table_name)
            .insert(device.model_dump(mode="json"))
            .execute()
        )
    
    def get_device_by_id(self, device_id: str):
        return (
            self.supabase.table(self.table_name)
            .select("*")
            .eq("device_key", device_id)
            .execute()
        )
    
    def verify_device_key(self, device_key: str):
        return (
            self.supabase.table(self.table_name)
            .select("*")
            .eq("device_key", device_key)
            .execute()
        )