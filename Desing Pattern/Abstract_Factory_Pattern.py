from abc import ABC,abstractmethod

class Computer(ABC):

    @abstractmethod
    def getHDD(self):
        pass

    @abstractmethod
    def getRAM(self):
        pass

    @abstractmethod
    def getCPU(self):
        pass

class PC(Computer):

    def __init__(self,h,r,c):
        self.hdd = h
        self.ram = r
        self.cpu = c

    def getHDD(self):
        return self.hdd

    def getRAM(self):
        return self.ram


    def getCPU(self):
        return self.cpu


class Server(Computer):

    def __init__(self,h,r,c):
        self.hdd = h
        self.ram = r
        self.cpu = c


    def getHDD(self):
        return self.hdd


    def getRAM(self):
        return self.ram


    def getCPU(self):
        return self.cpu


class AbstractFactory(ABC):

    @abstractmethod
    def createComputer(self,hd,rm,cp):
        pass


class PCFactory(AbstractFactory):

    def createComputer(self,hd,rm,cp):
        return PC(hd,rm,cp)

class ServerFactory(AbstractFactory):
    def createComputer(self,hd,rm,cp):
        return Server(hd,rm,cp)

class ComputerFacotry:

    @classmethod
    def createComputer(cls,typ,hd,ra,cp):
        if typ == 'PCF':
            return PCFactory().createComputer(hd,ra,cp)
        elif typ == 'ServerF':
            return ServerFactory().createComputer(hd,ra,cp)

p1 = ComputerFacotry.createComputer('PCF',80,2,'quadcore')

print(type(p1))

p2 = ComputerFacotry.createComputer('ServerF',800,8,'quadcore')
print(type(p2))
