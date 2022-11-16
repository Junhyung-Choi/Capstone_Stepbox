"""
# 캡스톤 스텝박스 신호 처리를 위한 파일

todo:
    1. 핀 번호랑 스위치 영역 매핑 (완료)
        2,  3: 1번 스위치
        4, 14: 2번 스위치
       15, 18: 3번 스위치
       17, 27: 4번 스위치
       22, 23: 5번 스위치
       24, 25: 6번 스위치
       10,  9: 7번 스위치
       11,  8: 8번 스위4
    2. 각 영역에 맞는 제어 함수 모듈화 하기
    3. 유닛 테스트 코드 작성
    4. LED 애니메이션 파일 모듈화
    5. LED 밝기 높일 수 있는 방법 찾아보기
    6. 신호 받아와서 유니티로 보낼 수 있는 방법 찾아보기?
"""

from enum import Enum
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup()
GPIO.setup()

leds    = [2,  4, 15, 17, 22, 24, 10, 11]
buttons = [3, 14, 18, 27, 23, 25,  9,  8]

try:
    while True:
        pass

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()