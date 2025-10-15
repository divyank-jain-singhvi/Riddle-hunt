from ultralytics import YOLO


model = YOLO("yolov8n.pt") 

model.train(data=r"C:\Users\divyank.singhvi\Divyank\ctc_code\demo\dataset.yaml", epochs=50, batch=16, imgsz=640)


