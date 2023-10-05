from abc import ABC, abstractmethod


class Tires(ABC):
    def __init__(self, tire_wear_sensors):
        self.tire_wear_sensors = tire_wear_sensors
    
    @abstractmethod
    def needs_service(self):
        pass
    
