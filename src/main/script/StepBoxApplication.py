from controller.systemcontroller import SystemController
import view
import model
import RPi.GPIO as GPIO

m_Controller = SystemController()

try:
    m_Controller.play()
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    GPIO.cleanup()