from abc import *

class Controller(metaclass = ABCMeta):
    isInited:bool = False
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def play(self):
        pass
