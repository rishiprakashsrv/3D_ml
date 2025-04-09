# utils/pointcloud_utils.py

import open3d as o3d
import numpy as np
from config import INTRINSICS
import cv2


def create_rgbd(depth, image):
    if depth.dtype != np.uint8:
        depth = (depth - depth.min()) / (depth.max() - depth.min()) * 255
        depth = depth.astype(np.uint8)

    if image.shape[:2] != depth.shape[:2]:
        image = cv2.resize(image, (depth.shape[1], depth.shape[0]))

    color_o3d = o3d.geometry.Image(image)
    depth_o3d = o3d.geometry.Image(depth)

    rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_o3d, depth_o3d,
        convert_rgb_to_intensity=False
    )

    return rgbd

def rgbd_to_pointcloud(rgbd_image):
    intrinsic = o3d.camera.PinholeCameraIntrinsic()
    intrinsic.set_intrinsics(**INTRINSICS)
    return o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsic)

def clean_pointcloud(pcd):
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=6.0)
    pcd = pcd.select_by_index(ind)
    pcd.estimate_normals()
    pcd.orient_normals_to_align_with_direction()
    return pcd
