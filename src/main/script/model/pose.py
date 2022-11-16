from abc import ABCMeta, abstractmethod
from typing import List, Tuple
from src.main.script.domain.sensor import Sensor

class PoseResult:
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value

class Pose(metaclass=ABCMeta):
    set:int = 0
    time:int = 0

    @abstractmethod
    def evalPosef(self,sensors:List[Sensor]) -> float:
        """
        동작을 평가하고, 그에 맞는 결과값을 주는 함수\n
        0.0 ~ 1.0 사이의 값을 리턴함.\n
        :param sensors:List[Sensor]
        :return: float
        """
        return 0.0

    @abstractmethod
    def evalPoseMsg(self,sensors:List[Sensor]) -> PoseResult:
        """
        동작을 평가하고, 그에 맞는 결과값을 주는 함수\n
        PoseResult를 리턴함 (value와 message를 리턴)\n
        :param sensors:List[Sensor]
        :return: PoseResult
        """
        return PoseResult("tmp",0.0)



