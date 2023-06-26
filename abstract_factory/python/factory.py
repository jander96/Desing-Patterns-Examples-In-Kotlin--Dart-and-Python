from abc import ABC, abstractmethod


class Silla(ABC):
    @abstractmethod
    def description(self) -> str:
        pass


class Sofa(ABC):
    @abstractmethod
    def description(self) -> str:
        pass


class Mesilla(ABC):
    @abstractmethod
    def description(self) -> str:
        pass



# Tenemos diferente variadades de estos productos Moderno y Victoriano 


# Juego de estilo Victoriano
class SillaVictoriana(Silla):
    
    def description(self) -> str:
        return 'silla victoriana'
    
class SofaVictoriano(Sofa):
    
    def description(self) -> str:
        return 'sofa victoriana'
    
class MesillaVictoriana(Mesilla):
    
    def description(self) -> str:
        return 'mesilla victoriana'

# Juego de estilo Moderno
class SillaModerna(Silla):
    
    def description(self) -> str:
        return 'silla moderna'
    
class SofaModerno(Sofa):
    
    def description(self) -> str:
        return 'sofa moderno'
    
class MesillaModerna(Mesilla):
    
    def description(self) -> str:
        return 'mesilla moderna'


class Factory(ABC) :
    @abstractmethod
    def crearSilla(self)-> Silla:
        pass
    
    @abstractmethod   
    def crearSofa(self)-> Sofa:
        pass
    
    @abstractmethod
    def crearMesilla(self)-> Mesilla:
        pass


    def combinarMuebles(self)-> str:
        return f"Juego de muebles \n Silla: {self.crearSilla().description()}\n Sofa: {self.crearSofa().description()}\n Mesilla: {self.crearMesilla().description()} "



class ModerFactory(Factory):

    def crearSilla(self)-> Silla:
        return SillaModerna()

    def crearSofa(self)-> Sofa:
        return SofaModerno()

    def crearMesilla(self)-> Mesilla:
        return MesillaModerna()



class VictorianFactory(Factory):

    def crearSilla(self)-> Silla:
        return SillaVictoriana()

    def crearSofa(self)-> Sofa:
        return SofaVictoriano()

    def crearMesilla(self)-> Mesilla:
        return MesillaVictoriana()

def main():
    entregarMuebles(ModerFactory())
    entregarMuebles(VictorianFactory())


def entregarMuebles(factory: Factory):
    print(factory.combinarMuebles())

if __name__ == "__main__":
    main()