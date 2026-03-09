from ultralytics import YOLO

model = YOLO("runs/detect/train10/weights/best.pt")

results = model("test_images/fire1.jpg", show=True)