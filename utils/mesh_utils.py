# utils/mesh_utils.py

import open3d as o3d
import numpy as np
from config import MESH

def reconstruct_mesh(pcd):

    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=MESH["depth"])[0]
    mesh = mesh.filter_smooth_laplacian(number_of_iterations=MESH["smooth_iterations"])
    rotation = mesh.get_rotation_matrix_from_xyz((np.pi, 0, 0))
    mesh.rotate(rotation, center=(0, 0, 0))
    return mesh

