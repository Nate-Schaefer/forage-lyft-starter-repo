from batteries.battery import Battery
from engines.engine import Engine
from Serviceable.serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.Engine = engine
        self.Battery = battery

    def needs_service(self):
        return self.Engine.needs_service() or self.Battery.needs_service()
