from typing import List

import src.main.script.model import pose
from src.main.script.domain.sensor import Sensor
from src.main.script.model.pose import PoseResult


class ClickPose(pose.Pose):
    def evalPosef(self, sensors: List[Sensor]) -> float:

        pass

    def evalPoseMsg(self, sensors: List[Sensor]) -> PoseResult:

        pass