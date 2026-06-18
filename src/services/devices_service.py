

from src.repositories.devices_repository import DevicesRepository


class DevicesService:
    def __init__(self):
        self.devices_repository = DevicesRepository()
        
    def create_device(self, device_data):
        return self.devices_repository.create_device(device_data)
    
    def get_device_by_id(self, device_id: str):
        return self.devices_repository.get_device_by_id(device_id)
    
    def verify_device_key(self, device_key: str):
        return self.devices_repository.verify_device_key(device_key)