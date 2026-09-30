"""Webcam loop: capture frame -> YOLOv8 inference -> show annotated frame."""

from ultralytics import YOLO
import cv2
import torch

from . import config


def main():
    # ------------------------------------------------------
    # 1️⃣ Check device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("🧠 Torch device:", device.upper())

    # ------------------------------------------------------
    # 2️⃣ Load the most accurate YOLOv8 model (runs fine on CPU)
    print("📦 Loading YOLOv8x model (most accurate, may take a few seconds)...")
    model = YOLO(config.MODEL_WEIGHTS)  # auto-downloads if not present

    # ------------------------------------------------------
    # 3️⃣ Start webcam feed
    cap = cv2.VideoCapture(config.CAM_INDEX)
    if not cap.isOpened():
        print("❌ Could not open webcam.")
        return

    print("📹 Webcam started — press 'q' to quit.")

    # ------------------------------------------------------
    # 4️⃣ Realtime detection loop
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Frame not received, exiting.")
            break

        # Run YOLO inference on the frame
        results = model(frame, imgsz=config.IMG_SIZE, device=device, verbose=False)

        # Annotate detections on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow(config.WINDOW_TITLE, annotated_frame)

        # Quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # ------------------------------------------------------
    # 5️⃣ Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("✅ Exited cleanly.")
