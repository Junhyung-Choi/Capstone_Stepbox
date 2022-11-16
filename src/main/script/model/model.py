from abc import ABCMeta, abstractmethod


class Model(metaclass=ABCMeta):
    @abstractmethod
    def getObject(self):
        pass

    @abstractmethod
    def getObjectById(self):
        pass

    @abstractmethod
    def saveObject(obj):
        pass

    @abstractmethod
    def delObjectById(id):
        pass