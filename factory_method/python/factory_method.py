from __future__ import annotations
from abc import ABC, abstractmethod

class DeliveryFactory(ABC):
    def __init__(self):
        self.vehicle = self.create_vehicle()
    @abstractmethod
    def create_vehicle(self)->Vehicle:
        pass
    
    def transportOrder(self):
        print( f"{self.vehicle.start_mov()} -- the order is moving in {self.vehicle} -- {self.vehicle.stop_mov()} ")
    
    def reparingVehicle(self):
        print("the $vehicle is in garage ")
    
    
class CarDeliveryTransportFactory(DeliveryFactory):
    
    def create_vehicle(self) -> Vehicle:
        return Car()
   
    
class BikeDeliveryTransportFactory(DeliveryFactory):
        
    def create_vehicle(self) -> Vehicle:
        return Bike()
    
      
class Vehicle(ABC):
    @abstractmethod
    def start_mov(self):
        pass
    @abstractmethod
    def stop_mov(self):
        pass
        
class Car(Vehicle):
    def start_mov(self):
        return "start engine"
    def stop_mov(self):
        return "stop engine"
    
    def __str__(self) -> str:
        return "Car"
    
    
class Bike(Vehicle):
    def start_mov(self):
        return "start pedal"
    def stop_mov(self):
        return "stop pedal"
    def __str__(self) -> str:
        return "Bike"
    
if __name__ == "__main__":
    carTransportation = CarDeliveryTransportFactory()
    bikeTransportation = BikeDeliveryTransportFactory()
        
    carTransportation.transportOrder()
    bikeTransportation.transportOrder()
    print("Hello my name is Jesus")
    