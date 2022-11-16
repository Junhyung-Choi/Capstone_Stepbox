import time

# Uncomment on Raspberry PI
import RPi.GPIO as GPIO

from .abstractcontroller import Controller
from domain.switchsensor import SwitchSensor

PIN_INDEX = [2,4,15,17,22,24,10,11]
class SystemController(Controller):
    """
    시스템의 전반적인 흐름을 컨트롤 한다.

    Functions:
        init: 프로그램 시작 시 1회만 호출됨. 설정 등을 추가하는 장소
        play: 프로그램 실행 내내 반복해서 호출되는 함수
    """
    sensors = []

    def init(self):
        print("Init Program")

        for i in range(8):
            self.sensors.append(SwitchSensor(i,PIN_INDEX[i]))


    def play(self):
        while True:
            if not self.isInited:
                self.init()
                self.isInited = True

            print("Program running...")


            for sensor in self.sensors:
                print(sensor)
            print("======================")

            time.sleep(10)








    