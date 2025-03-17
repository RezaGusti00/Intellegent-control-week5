from ultralytics import YOLO

# Load model YOLOv8 Pose
model = YOLO("yolov8n-pose.pt")

# Deteksi pose pada gambar
results = model("IMG_4492.jpg", show=True)

# Simpan hasil
results[0].save("IMG_4492.jpg")