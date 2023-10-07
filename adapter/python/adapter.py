from abc import ABC, abstractmethod

class SpecialLibrary():
    def getData(self):
        return "atad litu"


class Data(ABC):
    
    @abstractmethod    
    def getData(self):
        pass



class Adapter(Data):
    def __init__(self, library: SpecialLibrary):
        self.library  = library

    def getData(self):
        rawData: str = self.library.getData()
        return rawData.upper()
    





def main():
    specialLibrary = SpecialLibrary()
    adapter = Adapter(specialLibrary)
    data  = adapter.getData()
    print(data)



if __name__ == '__main__': 
    main()
