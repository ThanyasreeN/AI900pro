from ultralytics import YOLO
model=YOLO('yolov8n.pt')
model.predict(source="C://Users//nthan//Downloads//cat.jpg",save=True,show=True)
  