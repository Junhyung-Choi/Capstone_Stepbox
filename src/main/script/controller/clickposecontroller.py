from .posecontroller import PoseController
from model.pose import Pose
import time

class ClickPoseController(PoseController):
    def init(self):
        super().init()
        self.time = time.process_time_ns
    
    def play(self):
        try:
            print("Workout: Click")
            tensor = []
            while True:
                print("Checking Sensor Values...")
                now_time = time.process_time_ns()
                tensor.append((self.pose.sensors,(self.pose.sensors[i].posX,self.pose.sensors[i].posY)), now_time)
                self.pose.evalPoseTensor(tensor)               
                #self.pose.evalPoseMsg(self.pose.sensors)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Workout Ends: KeyboardInterrupt")
        finally:
            pass