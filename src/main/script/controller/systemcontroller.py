import time
from typing import Tuple, List

# Uncomment on Raspberry PI
import RPi.GPIO as GPIO

from .abstractcontroller import Controller
from domain.switchsensor import SwitchSensor
from domain.sensor import Sensor
from model.pose import Pose, PoseResult
from model.clickpose import ClickPose

PIN_INDEX: Tuple[int] = (2, 4, 15, 17, 22, 24, 10, 11)
OUT_PIN_INDEX: Tuple[int] = (3, 14, 18, 27, 23, 25, 9, 8)


class SystemController(Controller):
    """
    시스템의 전반적인 흐름을 컨트롤 한다.

    Functions:
        init: 프로그램 시작 시 1회만 호출됨. 설정 등을 추가하는 장소\n
        play: 프로그램 실행 내내 반복해서 호출되는 함수
    """
    sensors: List[Sensor] = []
    pose: Pose = None

    def init(self):
        print("Init Program (기존 운동 데이터 확인 / 운동 모드 선택 등등..)")

        GPIO.setmode(GPIO.BCM)
        
        # 테스트를 위해 1로 조정
        for i in range(1):
            GPIO.setup(PIN_INDEX[i], GPIO.IN)
            GPIO.setup(OUT_PIN_INDEX[i], GPIO.OUT)
        
        # 테스트를 위해 1로 조정
        for i in range(1):
            self.sensors.append(SwitchSensor(i, PIN_INDEX[i]))

        # 테스트를 위해 pose를 ClickPose로 조정
        self.pose = ClickPose()

    def play(self):
        self.init()
        print("Program running...")
        while True:

            self.pose.evalPosef(self.sensors)
            # for sensor in self.sensors:
            #     print(sensor)
            # print("======================")

            time.sleep(0.5)
