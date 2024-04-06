import pyautogui

from ultralytics import YOLO
import time

model = YOLO("Yolov8nano.pt")
while True:
    screenshot = pyautogui.screenshot(region=(0,0,500,400))
    results = model.predict(source=screenshot, imgsz=320, conf=0.4, classes = [2], save =True)
    r = results[0]
    boxes = r.boxes.cpu().numpy()
    xyxys = boxes.xyxy
    for xyxy in xyxys: #for Detections
        x1,y1,x2,y2 = boxes.xyxy[0] 
                
        center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2 #find center of box
                
            
        pyautogui.moveTo(center_x,center_y+5) #Swipe Fruit
        pyautogui.dragTo(center_x, (center_y-110),duration=0.105, button = "left")

    
        
            


