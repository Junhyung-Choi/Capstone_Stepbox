from abc import *

class Sensor(metaclass=ABCMeta):
    
    def __init__(self, index):
        self.index = index
        pass

    value = 0.0

    @abstractmethod
    def getval(self):
        return self.value

    @abstractmethod
    def setval(self):
        return self.value