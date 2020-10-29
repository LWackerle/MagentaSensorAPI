import requests
from datetime import datetime


class API_Manager:
    def __init__(self, base_url):
        self.base_url = base_url

    # Public Methods
    def update_device_status(self, device_id, occupied):
        device = {
            "device_id": device_id,
            "occupied": occupied,
            "last_update": datetime.utcnow().isoformat()
        }
        url = self.base_url+'/devices'
        return requests.post(url, json=device)

    def add_to_history(self, device_id, occupied, gateway):
        device = {
            "device_id": device_id,
            "timestamp": datetime.utcnow().isoformat(),
            "occupied": occupied,
            "gateway": gateway
        }
        url = self.base_url+"/history"
        return requests.post(url, json=device)
