# utils/vis_utils.py

import matplotlib.pyplot as plt
import open3d as o3d

def show_depth_and_image(image, depth):
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(image)
    ax[0].axis('off')
    ax[1].imshow(depth, cmap='plasma')
    ax[1].axis('off')
    plt.tight_layout()
    plt.pause(3)

def show_pointcloud(pcd):
    o3d.visualization.draw_geometries([pcd])

def show_mesh(mesh):
    o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)
