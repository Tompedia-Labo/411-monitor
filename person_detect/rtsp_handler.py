import cv2
from models import CameraAuth

class RTSPStream:
    def __init__(self, CameraAuth):
        print(CameraAuth.user!="" and CameraAuth.password!="")
        if CameraAuth.user!="" and CameraAuth.password!="":
            print("!!!!!!!!!!!!")
            self.url_with_auth = f"rtsp://{CameraAuth.user}:{CameraAuth.password}@{CameraAuth.url}"
        else:
            self.url_with_auth = f"rtsp://{CameraAuth.url}"

        self.cap = cv2.VideoCapture(self.url_with_auth)

        if not self.cap.isOpened():
            raise ValueError(f"Couldn't open RTSP stream!: {self.url_with_auth}")


    def frames(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            yield frame
    
    def release(self):
        self.cap.release()
