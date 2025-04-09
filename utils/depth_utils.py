# utils/depth_utils.py

import numpy as np
import cv2
from PIL import Image

def postprocess_depth(predicted_depth, original_image, pad=16):
    image_np = np.array(original_image)


    output = np.squeeze(predicted_depth) * 1000.0  
    output = output[pad:-pad, pad:-pad]

    depth_high_res = cv2.resize(output, (output.shape[1] * 2, output.shape[0] * 2), interpolation=cv2.INTER_CUBIC)

    depth_filtered = cv2.bilateralFilter(depth_high_res.astype(np.float32), d=9, sigmaColor=75, sigmaSpace=75)

    depth_filtered_norm = (depth_filtered - depth_filtered.min()) / (depth_filtered.max() - depth_filtered.min()) * 255
    depth_filtered_norm = depth_filtered_norm.astype(np.uint8)

    new_height, new_width = depth_filtered.shape
    image_resized = cv2.resize(image_np, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    return depth_filtered.astype(np.float32), image_resized
