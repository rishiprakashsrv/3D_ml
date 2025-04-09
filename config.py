# config.py

MODEL_NAME = "Intel/dpt-large"
DEVICE = "mps"  # 'cuda' if on GPU, 'cpu' fallback
RESIZE_HEIGHT = 720
BICUBIC_SCALE = 2
BILATERAL_FILTER = True

INTRINSICS = {
    "fx": 1000,
    "fy": 1000,
    "cx": 480,
    "cy": 360,
    "width": 960,
    "height": 720,
}

MESH = {
    "depth": 12,
    "smooth_iterations": 5
}
