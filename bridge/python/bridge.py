from abc import ABC , abstractmethod

def main() :
    device = TV()

    basicControl = TvBasicControl(device)
    print(f"TV State -> isTurnOn: {device.isEnable} Volume: {device.vol}, Channel: {device.chan}")
    basicControl.tooglePower()
    basicControl.volumeUp()
    basicControl.channelUp()
    print(f"TV State -> isTurnOn: {device.isEnable} Volume: {device.vol}, Channel: {device.chan}")



class Device(ABC) :

    isEnable: bool
    chan: int
    vol: int
    
    @abstractmethod
    def enable(self):
        pass
    
    @abstractmethod
    def disable(self):
        pass
    
    @abstractmethod
    def getVolume(self)->int:
        pass
    
    @abstractmethod
    def setVolume(self,percent: int):
        pass
    
    @abstractmethod
    def getChannel(self,) -> int:
        pass
    
    @abstractmethod
    def setChannel(self,number: int):
        pass


class RemoteControl(ABC):
    @abstractmethod
    def tooglePower(self):
        pass
    
    @abstractmethod
    def volumeDown(self):
        pass
    
    @abstractmethod
    def volumeUp(self):
        pass
    
    @abstractmethod
    def channelDown(self):
        pass
    
    @abstractmethod
    def channelUp(self):
        pass


class TV (Device):

    isEnable: bool = False

    chan: int = 0

    vol: int = 0

    def enable(self):
        print("Power on")
        self.isEnable = True
    

    def disable(self):
        print("Power off")
        self.isEnable = False
    

    def getVolume(self)-> int:
        print("Getting volume")
        return self.vol
    

    def setVolume(self, percent: int):
        self.vol = self.getVolume() + percent
    

    def getChannel(self)-> int:
        print("Getting channel ")
        return self.chan
    

    def setChannel(self, number: int):
        self.chan = self.getChannel() + number
    


class TvBasicControl(RemoteControl) :
    
    def __init__(self,device: Device):
        self.device = device

    def tooglePower(self): 
        if self.device.isEnable:
            self.device.disable()
        else: 
            self.device.enable()
        
    

    def volumeDown(self):
        self.device.setVolume(-10)
    

    def volumeUp(self):
        self.device.setVolume(10)
    

    def channelDown(self):
        self.device.setChannel(-1)
    

    def channelUp(self):
        self.device.setChannel(1)
    



class TvModernControl(RemoteControl) :

    def __init__(self,device: Device):
        self.device = device

    def tooglePower(self): 
        if self.device.isEnable:
            self.device.disable()
        else: 
            self.device.enable()
        
    

    def volumeDown(self):
        self.device.setVolume(-10)
    

    def volumeUp(self):
        self.device.setVolume(10)
    

    def channelDown(self):
        self.device.setChannel(-1)
    

    def channelUp(self):
        self.device.setChannel(1)

    # Others advance functions
    def mute(self):
        self.device.setVolume(0)
    
if __name__ == "__main__":
    main()