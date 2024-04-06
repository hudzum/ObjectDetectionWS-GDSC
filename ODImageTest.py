from ultralytics import YOLO

model = YOLO("Yolov8small.pt")

result = model.predict(source = "SampleImage.png", imgsz=640, conf=0.7, save =True)