import cv2
from models import CameraAuth

class RTSPStream:
    def __init__(self, CameraAuth):
        self.cap = cv2.VideoCapture(CameraAuth.url)

        if CameraAuth.user!="" and CameraAuth.password!="":
            self.url_with_auth = f"rtsp://{CameraAuth.user}:{CameraAuth.password}@{CameraAuth.url}"
        else:
            self.url_with_auth = f"rtsp://{CameraAuth.url}"

        if not self.cap.isOpened():
            raise ValueError(f"Couldn't open RTSP stream!: {CameraAuth.url}")

    def frames(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            yield frame
