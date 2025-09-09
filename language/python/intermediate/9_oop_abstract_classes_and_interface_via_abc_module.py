from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass
    
    def fuel_type(self):
        print("Unknown fuel")
    
class Car(Vehicle):
    def start_engine(self):
        print("Car Engine Started")

    def fuel_type(self):
        print("Petrol")

class ElectricScooter(Vehicle):
    def start_engine(self):
        print("Electric scooter powered on")

    def fuel_type(self):
        print("Electric")

car = Car()
car.start_engine()
car.fuel_type()
scooter = ElectricScooter()
scooter.start_engine()
scooter.fuel_type()
