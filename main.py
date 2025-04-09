# main.py

import os
import open3d as o3d
from models.depth_model import load_model, predict_depth
from utils.image_utils import load_and_resize, enhance_image
from utils.depth_utils import postprocess_depth
from utils.pointcloud_utils import create_rgbd, rgbd_to_pointcloud, clean_pointcloud
from utils.mesh_utils import reconstruct_mesh
from utils.vis_utils import show_depth_and_image, show_pointcloud, show_mesh

def main(image_path):
    processor, model = load_model()

    image = load_and_resize(image_path)
    enhanced_img = enhance_image(image)

    depth = predict_depth(model, processor, image)
    
    from utils.depth_utils import postprocess_depth

    refined_depth, processed_img = postprocess_depth(depth, enhanced_img)
    show_depth_and_image(processed_img, refined_depth)



    rgbd = create_rgbd(refined_depth, enhanced_img)
    pcd = rgbd_to_pointcloud(rgbd)
    pcd = clean_pointcloud(pcd)
    show_pointcloud(pcd)

    mesh = reconstruct_mesh(pcd)
    show_mesh(mesh)
    print("[MESH] Saving mesh to 'output_mesh.ply'...")
    o3d.io.write_triangle_mesh("output_mesh.ply", mesh)

        


if __name__ == "__main__":
    main("DATA/img4.jpg")
