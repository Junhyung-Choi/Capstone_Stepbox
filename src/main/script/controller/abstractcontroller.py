from abc import *

class Controller(metaclass = ABCMeta):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def play(self):
        pass
