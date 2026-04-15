from ultralytics import YOLO

class PersonDetector:
    def __init__(self, model_path="yolov8n.pt", person_class=0, conf_threshold=0.3):
        self.model = YOLO(model_path)
        self.person_class = person_class
        self.conf_threshold = conf_threshold

    def detect(self, frame):
        """人物のバウンディングボックスのリストを返す"""
        results = self.model(frame)
        persons = []
        for box in results[0].boxes:
            if int(box.cls) == self.person_class and float(box.conf) >= self.conf_threshold:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                persons.append((x1, y1, x2, y2))
        return persons
