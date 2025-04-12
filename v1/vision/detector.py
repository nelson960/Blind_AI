from ultralytics import YOLO
import cv2

class ObjectDetector:
	def __init__(self):
		self.model = YOLO("/Users/nelson/py/ml_App/blind_ai/models/yolov8n.pt")
		self.model.fuse()

	def detect_objects(self, frame):
		results = self.model.predict(source=frame, imgsz=416, conf=0.5, verbose=False)
		boxes = results[0].boxes
		labels = []
		if boxes:
			for box in boxes:
				cls_id = int(box.cls[0])
				label = self.model.names[cls_id]
				labels.append(label)
			return labels