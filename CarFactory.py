from batteries.NubbinBattery import NubbinBattery
from batteries.SpindlerBattery import SpindlerBattery
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from car import Car


class CarFactory():

    @staticmethod
    def create_calliope(current_service_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_service_date, last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_glissade(current_service_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_service_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_service_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_service_date, last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(current_service_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_service_date, last_service_date)
        return Car(engine, battery)
    
    @staticmethod
    def create_thovex(current_service_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_service_date, last_service_date)
        return Car(engine, battery)

    
        
