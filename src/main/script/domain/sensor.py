from abc import *

class Sensor(metaclass=ABCMeta):
    
    def __init__(self, index, pinnum):
        self.index = index
        self.pinnum = pinnum

    def __str__(self):
        return "Sensor " + str(self.index) + " / Pin number :" + str(self.pinnum)

    value = 0.0
    @abstractmethod
    def getvalue(self):
        return self.value

    @abstractmethod
    def setvalue(self,value):
        self.value = value;

    @abstractmethod
    def getValueFromDevice(self):
        # GPIO.input(self.pinnum)
        return self.value