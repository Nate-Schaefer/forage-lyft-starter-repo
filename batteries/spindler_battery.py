from abc import ABC
from battery import Battery
from datetime import datetime


class SpindlerBattery(Battery, ABC):
    def __init__(self, current_service_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_service_date = current_service_date
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return service_threshold_date < self.current_service_date