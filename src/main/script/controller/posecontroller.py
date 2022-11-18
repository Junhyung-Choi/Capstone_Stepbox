from model.pose import Pose
from .abstractcontroller import Controller

class PoseController(Controller):
    """
    각 포즈별로 새로 만드는 컨트롤러
    포즈의 동작을 PoseController의 play문이 반복문을 통해 새로운 플레이 씬을 동작시킨다.
    상속용 클래스
    """
    def __init__(self, pose:Pose) -> None:
        super().__init__()
        self.pose:Pose = pose

    def init(self):
        return super().init()
    
    def play(self):
        return super().play()
