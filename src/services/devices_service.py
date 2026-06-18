

class DevicesService:
    def __init__(self, devices_repository):
        self.devices_repository = devices_repository

    def create_device(self, device_data):
        return self.devices_repository.create_device(device_data)
    
    def get_device_by_key(self, device_key: str):
        return self.devices_repository.get_device_by_key(device_key)
    