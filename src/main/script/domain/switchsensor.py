from . import sensor
import RPi.GPIO as GPIO

class SwitchSensor(sensor.Sensor):
    def __init__(self, index, pinnum):
        super().__init__(index, pinnum)

    def __str__(self):
        return super().__str__()

    def getvalue(self):
        return self.value

    def setvalue(self,value):
        self.value = value

    def getValueFromDevice(self):
        self.value = GPIO.input(self.pinnum)
        # print("Value: " + str(self.value) + " Pin number: " + str(self.pinnum))
        return self.value




