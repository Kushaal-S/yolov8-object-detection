# YOLOv8 Live Camera Detection

Real-time object detection from your webcam using [Ultralytics YOLOv8](https://docs.ultralytics.com/). It loads the most accurate model in the family (**YOLOv8x**), runs it on every frame, and shows the camera feed with bounding boxes, class labels and confidence scores drawn on top.

<!-- Add a demo GIF here:  ![Demo](docs/demo.gif) -->

## Features

- Live detection from a webcam
- Automatically uses your **GPU (CUDA)** if available, otherwise the CPU
- Uses YOLOv8x at 960 px inference size
- Detects the 80 everyday object classes of the COCO dataset (people, cars, cups, laptops, animals…)
- Model weights download automatically on first run

## Requirements

- Python 3.9+
- A webcam
- Internet connection on first run (to download the model weights)
- A CUDA-capable GPU is strongly recommended — YOLOv8x is the largest model and can be slow on a CPU

## Installation

```bash
git clone https://github.com/<your-username>/yolov8-live-detection.git
cd yolov8-live-detection

python -m venv .venv
# Windows:      .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate

pip install -r requirements.txt
```

> **Using an NVIDIA GPU?** Install the CUDA build of PyTorch first by following the selector at [pytorch.org](https://pytorch.org/get-started/locally/), then run `pip install -r requirements.txt`.

## Usage

```bash
python YOLOv8_Demonstration.py
# or
python -m yolov8_demo
```

On startup it prints which device it's using, loads the model, and opens a window called **"YOLOv8x - Live Camera Detection"**. Press **`q`** in that window to quit.

## Configuration

Settings live in [`yolov8_demo/config.py`](yolov8_demo/config.py):

| Setting | Default | Description |
|---|---|---|
| `CAM_INDEX` | `0` | Which webcam to use. Try `1`, `2`… if you have several. |
| `MODEL_WEIGHTS` | `"yolov8x.pt"` | Model file. Downloaded automatically if missing. |
| `IMG_SIZE` | `960` | Inference image size. Smaller is faster, larger can catch smaller objects. |
| `WINDOW_TITLE` | `"YOLOv8x - Live Camera Detection"` | Title of the display window. |

**Running slowly?** Switch to a lighter model, for example `MODEL_WEIGHTS = "yolov8n.pt"` (fastest) or `"yolov8s.pt"`, and/or lower `IMG_SIZE` to `640`. The available sizes are `n`, `s`, `m`, `l` and `x`, from fastest to most accurate.

## Project structure

```
yolov8-live-detection/
├── YOLOv8_Demonstration.py   # Launcher: python YOLOv8_Demonstration.py
├── yolov8_demo/
│   ├── __main__.py           # Launcher: python -m yolov8_demo
│   ├── app.py                # Webcam loop + YOLOv8 inference
│   └── config.py             # Settings
├── requirements.txt
├── LICENSE
└── README.md
```

## How it works

1. Picks `cuda` if PyTorch can see a GPU, otherwise `cpu`.
2. Loads the YOLOv8 weights (downloading them if needed).
3. Reads frames from the webcam with OpenCV.
4. Runs the model on each frame and draws the detections with `results[0].plot()`.
5. Displays the annotated frame until you press `q`, then releases the camera and closes the window.

## Troubleshooting

- **`Could not open webcam.`** — Another app may be using the camera, or it has a different index. Change `CAM_INDEX` in `config.py`.
- **Very low frame rate** — You're probably running on the CPU. Use a GPU build of PyTorch or a smaller model (see Configuration).
- **Prints `Torch device: CPU` even though you have an NVIDIA GPU** — You likely installed the CPU-only PyTorch build. Reinstall PyTorch using the selector at [pytorch.org](https://pytorch.org/get-started/locally/).
- **macOS: black window or no camera** — Grant your terminal (or IDE) *Camera* permission in System Settings → Privacy & Security.

## Licensing note

This project's code is released under the [MIT License](LICENSE). It depends on [Ultralytics](https://github.com/ultralytics/ultralytics) and its YOLOv8 models, which are licensed separately (AGPL-3.0, with a commercial option). Check their license terms if you plan to use this commercially.
