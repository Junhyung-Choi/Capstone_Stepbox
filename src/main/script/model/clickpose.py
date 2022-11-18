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
        for index in self.sensor_list:
            value = sensors[index].getValueFromDevice()
            print("Click Pose Sensor Index: " + str(index) + " / Sensor Value: " + str(value))
        return pose.PoseResult("tmp",1)
        