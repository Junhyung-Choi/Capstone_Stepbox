import time
from typing import Tuple, List

# Uncomment on Raspberry PI
import RPi.GPIO as GPIO

from .abstractcontroller import Controller
from domain.switchsensor import SwitchSensor
from domain.sensor import Sensor
from model.pose import Pose, PoseResult
from model.clickpose import ClickPose
from controller.posecontroller import PoseController
from controller.clickposecontroller import ClickPoseController

PIN_INDEX: Tuple[int] = (2, 4, 15, 17, 22, 24, 10, 11)
OUT_PIN_INDEX: Tuple[int] = (3, 14, 18, 27, 23, 25, 9, 8)


class SystemController(Controller):
    """
    시스템의 전반적인 흐름을 컨트롤 한다.

    Functions:
        init: 프로그램 시작 시 1회만 호출됨. 설정 등을 추가하는 장소\n
        play: 프로그램을 돌리는 함수
    """
    sensors: List[Sensor] = []
    pose_controller: PoseController = None
    t:float

    def init(self):
        print("Init Program (기존 운동 데이터 확인 / 운동 모드 선택 등등..)")

        GPIO.setmode(GPIO.BCM)
        
        # 테스트를 위해 1로 조정
        for i in range(1):
            GPIO.setup(PIN_INDEX[i], GPIO.IN)
            GPIO.setup(OUT_PIN_INDEX[i], GPIO.OUT)
        
        t = time.process_time_ns()

        # 테스트를 위해 1로 조정
        for i in range(1):
            self.sensors.append(SwitchSensor(i, PIN_INDEX[i]))

        # 테스트를 위해 pose를 ClickPose로 조정
        self.pose_controller = ClickPoseController(ClickPose(self.sensors))
    
    def workout(self):
        print("Workout Controlling...")
        self.pose_controller.play()
        print("Workout End...")


    def play(self):
        self.init()
        print("Program running...")

        self.workout()

        print("Program End...")
