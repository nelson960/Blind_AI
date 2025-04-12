from ultralytics import YOLO
from collections import defaultdict

class YOLOv11Detector:
    def __init__(self):
        self.model = YOLO("models/yolo11s.pt")
        self.model.fuse()

    def detect_objects(self, frame):
        results = self.model.predict(source=frame, imgsz=640, conf=0.4, verbose=False)
        boxes = results[0].boxes
        width = frame.shape[1]

        position_map = defaultdict(list)

        for box in boxes:
            cls_id = int(box.cls[0])
            label = self.model.names[cls_id]
            x_center = float(box.xywh[0][0])
            box_area = float(box.xywh[0][2] * box.xywh[0][3])
            norm_area = box_area / (frame.shape[0] * frame.shape[1])  # Normalize size

            if x_center < width * 0.33:
                pos = "left"
            elif x_center > width * 0.66:
                pos = "right"
            else:
                pos = "center"

            position_map[(label, pos)].append(norm_area)

        descriptions = []
        for (label, pos), areas in position_map.items():
            size = max(areas)
            proximity = "close" if size > 0.15 else "far"
            descriptions.append(f"{label} on the {pos} ({proximity})")

        return descriptions
