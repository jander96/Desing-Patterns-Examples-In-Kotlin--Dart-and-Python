from abc import ABC, abstractmethod

def main():
    item = Circle(radius = 4)
    item.move(3, 3)
    item.draw()

    item2 = Compose()
    item2.add(Dot())
    item2.add(Dot(4,6))
    item2.add(Circle(5,5,5))
    item2.move(5, 5)
    item2.draw()



class Graphic(ABC):
    @abstractmethod
    def move(x: int, y : int):
        pass
    
    @abstractmethod
    def draw():
        pass


class Dot(Graphic):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def move(self, x: int, y: int):
        self.x += x
        self.y += y
     

    def draw(self):
        print(f"Estoy dibujando un punto entre ${self.x} y ${self.y}")
    


class Circle(Graphic):

    def __init__(self,radius: int, x = 0 , y = 0) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, x: int, y: int):
        self.x += x
        self.y += y
     

    def draw(self):
        print(f"Estoy dibujando un punto entre {self.x} y {self.y} con radio {self.radius}")
    



class Compose(Graphic): 
    
    def __init__(self) -> None:
        super().__init__()
        self.children: list[Graphic] = []

    def move (self,x: int, y: int):
        for child in self.children:
            child.move(x,y)
     
    def draw (self):
        for child in self.children:
            child.draw()
     

    

    def add(self,child: Graphic):
        self.children.append(child)

    def remove(self, child: Graphic):
        self.children.remove(child)
    

if __name__ == "__main__":
    main()

