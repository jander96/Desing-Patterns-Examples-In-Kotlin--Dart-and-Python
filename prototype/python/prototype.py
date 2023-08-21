

from abc import ABC, abstractmethod

class Prototye(ABC,):
    
    @abstractmethod
    def clone(self):
        pass


class File(Prototye):
    def __init__(self, name: str, content: str):
        self.name = name
        self._content = content
        
    def showInfo(self):
        print(f"Archivo ~~{self.name}~~ tiene como contenido -> {self._content}")
    
    def clone(self):
        return self


def main():
    file1 = File('precios', 'Listado de precios topados para el 2024')
    fileCopia = file1.clone()
    
    file1.showInfo()
    fileCopia.showInfo()
        
if __name__ == '__main__': 
    main()