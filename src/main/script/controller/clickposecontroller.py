from .posecontroller import PoseController
from model.pose import Pose
import time

class ClickPoseController(PoseController):
    def init(self):
        return super().init()
    
    def play(self):
        try:
            print("Workout: Click")
            while True:
                print("Checking Sensor Values...")
                self.pose.evalPoseMsg(self.pose.sensors)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Workout Ends: KeyboardInterrupt")
        finally:
            pass