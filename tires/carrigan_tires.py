from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear_sensors):
        super.__init__(tire_wear_sensors)
    
    
    def needs_service(self):
        for i in self.tire_wear_sensors:
            if i >= 0.9:
                return True
        return False
    
