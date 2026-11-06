from ultralytics import YOLO


class YoloDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        result = self.model(frame, conf=0.5, verbose=False)[0]
        if not len(result.boxes):
            return None, 0, frame

        x1, y1, x2, y2 = result.boxes[0].xyxy[0].tolist()
        width, height = int(x2 - x1), int(y2 - y1)
        bbox = (int(x1), int(y1), width, height)
        return bbox, width * height, result.plot()
