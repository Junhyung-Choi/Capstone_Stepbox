from abc import *

class Controller(metaclass = ABCMeta):
    @abstractmethod
    def play():
        pass
