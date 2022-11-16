import time
from typing import Tuple, List

# Uncomment on Raspberry PI
import RPi.GPIO as GPIO

from .abstractcontroller import Controller
from domain.switchsensor import SwitchSensor
from domain.sensor import Sensor

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

    def init(self):
        print("Init Program")

        """
        GPIO.setmode(GPIO.BCM)
        
        for i in range(8):
            GPIO.setup(PIN_INDEX(i, GPIO.IN)
            GPIO.setup(OUT_PIN_INDEX(i, GPIO.OUT)
        """
        for i in range(8):
            self.sensors.append(SwitchSensor(i, PIN_INDEX[i]))

    def play(self):
        while True:
            if not self.isInited:
                self.init()
                self.isInited = True

            for sensor in self.sensors:
                sensor.getValueFromDevice()

            print("Program running...")

            for sensor in self.sensors:
                print(sensor)
            print("======================")

            time.sleep(10)
