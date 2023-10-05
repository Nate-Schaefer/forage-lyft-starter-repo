from batteries.NubbinBattery import NubbinBattery
from batteries.SpindlerBattery import SpindlerBattery
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from car import Car


class CarFactory():

    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine, battery)

    
        
