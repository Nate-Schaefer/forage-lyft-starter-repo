from battery.battery import Battery
from engine.engine import Engine


class Car():
    def __init__(self, last_service_date):
        self.Engine = Engine
        self.Battery = Battery
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        if self.Engine.needs_service() or self.Battery.needs_service():
            return True
        else:
            return False
