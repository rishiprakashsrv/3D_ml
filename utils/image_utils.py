# utils/image_utils.py

from PIL import Image
import numpy as np
import cv2
from config import RESIZE_HEIGHT

def load_and_resize(image_path):
    image = Image.open(image_path)
    new_height = RESIZE_HEIGHT - (RESIZE_HEIGHT % 32)
    new_width = int(new_height * image.width / image.height)
    new_width -= new_width % 32
    return image.resize((new_width, new_height))

def enhance_image(image):
    image = np.array(image)
    image = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
    return image
