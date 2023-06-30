from abc import ABC, abstractmethod


    
class Automovil:
    
    def __init__(self,engine: str = "Standar", doors: int = 4, wheel: int = 4):
        self.engine = engine
        self.doors = doors
        self.wheel = wheel
        
    def __str__(self) -> str:
        return f"Automovil( engine = {self.engine}, doors = {self.doors}, wheel = {self.wheel} )"

class Manual:
    def __init__(self, descriptions: list[str] = []):
        self.descriptions = descriptions
    
    def __str__(self) -> str:
        return f"Manual = {self.descriptions} )"

class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def makeDoors(self,doors: int):
        pass
    
    @abstractmethod
    def setWheels(self,wheel: int):
        pass
    
    @abstractmethod
    def setEngine(self,engine: str):
        pass


class CarBuilder(Builder):
    car: Automovil = Automovil()
    
    def reset(self):
        self.car = Automovil()
    

    def makeDoors(self,doors: int)-> Builder:
        self.car.doors = doors
        return self
    

    def setWheels(self,wheel: int)-> Builder:
        self.car.wheel = wheel
        return self
    

    def setEngine(self,engine: str)-> Builder:
        self.car.engine = engine
        return self
    

    def build(self)-> Automovil:
        # Reset objet is optional when is build
        automovil = self.car
        self.reset()
        return automovil
    
class ManualBuilder(Builder):
    manual: Manual = Manual()
    
    def reset(self):
        self.manual = Manual()
    

    def makeDoors(self,doors: int)-> Builder:
        self.manual.descriptions.append(f"Car has {doors} doors")
        return self
    

    def setWheels(self,wheel: int)-> Builder:
        self.manual.descriptions.append(f"Car has {wheel} wheel")
        return self
    

    def setEngine(self,engine: str)-> Builder:
        self.manual.descriptions.append(f"Car has {engine} engine")
        return self
    

    def build(self)-> Automovil:
        return self.manual
    




class Director:
    def __init__(self,builder: Builder):
        self.builder  = builder

    def getDeportiveCarBuilder(self)-> Builder:
        return self.builder.setEngine("Deportive").makeDoors(2).setWheels(4)
    

    def getTruckBuilder(self)->Builder:
        return self.builder.setEngine("big").makeDoors(2).setWheels(8)


    
def main():
    # using builder with director class
    carBuilder = CarBuilder()
    director = Director(carBuilder)
    deportiveBuilder = director.getDeportiveCarBuilder().build()
    truckBuilder = director.getTruckBuilder().build()

    print(deportiveBuilder)

    print(truckBuilder)

    #using only builder

    manualBuilder = ManualBuilder()

    manual = (manualBuilder.setEngine("Deportive").makeDoors(2).setWheels(4)).build()
    print(manual)

if __name__ == '__main__': 
    main()