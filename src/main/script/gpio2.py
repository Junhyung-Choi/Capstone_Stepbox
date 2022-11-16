# 라이브러리 임포트
import RPi.GPIO as GPIO

# 어떤 모드로 쓸 건지에 대한 설명
# GPIO.BCM -> GPIO 핀 번호로 가져가겠다 이말임 (GPIO14 이런거 (실제 핀번호 : 8))
# GPIO.BOARD -> 실제 보드 핀 번호로 가져가겠다 이말임
GPIO.setmode(GPIO.BCM)

# 사용할 핀 번호 및 모드를 명시
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.OUT)


# 아두이노의 loop 함수와 비슷한 역할을 하는 부분
try:
    while True:
        # GPIO.input -> 핀 번호로부터 입력을 받아오는 함수
        inp = GPIO.input(14)
        print(inp)
        if(inp):
            # GPIO.output -> 핀 번호로 출력을 하는 함수
            GPIO.output(15,GPIO.LOW)
        else:
            GPIO.output(15,GPIO.HIGH)
# Ctrl + C키를 누르면 종료 됩니다.
except KeyboardInterrupt:
    # 종료시 LED를 무조건 끄기
    print("Program ended")

# GPIO 클린업
finally:
    GPIO.cleanup()