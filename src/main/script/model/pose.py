from abc import ABCMeta, abstractmethod
from typing import List, Tuple
from domain.sensor import Sensor

class PoseResult:
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value

class Pose(metaclass=ABCMeta):
    """
    pose쪽으로 sensor들을 일괄적으로 넘기고
    각 포즈가 필요한 센서의 값만 attribute를 통해 입력을 확인하고
    이걸 평가하는 과정이 필요함.

    다만 입력이 연속적으로 들어오고 이를 처리해야 하기 때문에 어떻게 할지 고민중 
    """
    set:int = 0
    time:int = 0
    
    sensors= []

    def __init__(self, sensors:List[Sensor]) -> None:
        self.sensors = sensors

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



