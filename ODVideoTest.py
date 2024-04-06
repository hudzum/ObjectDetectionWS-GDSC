from ultralytics import YOLO

model = YOLO("Yolov8nano.pt") #Loading pretrained Yolov8n

result = model.predict(source = "SampleGameplay.mp4", imgsz=640, conf=0.7, save =True) #Running a prediction on "SampleGameplay.mp4"gi