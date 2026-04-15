import cv2
import threading
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

        self.frame_lock = threading.Lock()
        self.latest_frame = None
        self.running = True
        self.thread = threading.Thread(target=self._update_frames, daemon=True)
        self.thread.start()

    def _update_frames(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                with self.frame_lock:
                    self.latest_frame = frame

    def frame(self):
        with self.frame_lock:
            return self.latest_frame.copy() if self.latest_frame is not None else None

    def release(self):
        self.cap.release()
