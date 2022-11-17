from typing import List

from . import pose
from domain.sensor import Sensor


class ClickPose(pose.Pose):

    sensor_list = [0]
    def evalPosef(self, sensors: List[Sensor]) -> float:
        print("Click Pose evalutate Pose / return float")
        pass

    def evalPoseMsg(self, sensors: List[Sensor]) -> pose.PoseResult:
        print("Click Pose evalutate Pose / return float with messages")
        pass