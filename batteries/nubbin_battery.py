from abc import ABC
from battery import Battery


class NubbinBattery(Battery, ABC):
    def __init__(self, current_service_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_service_date = current_service_date
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < self.current_service_date