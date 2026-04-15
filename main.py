from config import Config
from api.discord_webhook import send_discord_message
from person_detect.detector import PersonDetector
from person_detect.rtsp_handler import RTSPStream
from person_detect.utils import draw_boxes
import cv2

def main():
    stream = RTSPStream(Config.CAMERAS[0])
    detector = PersonDetector()
    count = 0
    try:
        for frame in stream.frames():
            boxes = detector.detect(frame)
            frame = draw_boxes(frame, boxes)
            if count != len(boxes):
                count = len(boxes)
                print(send_discord_message(f"411には{count}人います！"))
            
            cv2.putText(frame, f"People: {count}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.imshow("CamCount", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        stream.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
