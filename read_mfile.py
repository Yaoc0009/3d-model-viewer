import open3d as o3d
import numpy as np

filename = 'assets/bunny.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

v = []
f = []

for line in lines:
    line_split = line.strip().split()
    if line_split[0] == 'Vertex':
        v.append([float(line_split[2]), float(line_split[3]), float(line_split[4])])
    elif line_split[0] == 'Face':
        f.append([int(line_split[2]), int(line_split[3]), int(line_split[4])])

v = np.array(v)
f = np.array(f)
print("Number of Vertices: ", len(v))
print("Number of Faces: ", len(f))

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(v)
pcd.paint_uniform_color([0.5, 0.5, 0.5])
print(pcd)
print(np.asarray(pcd.points))
print(np.asarray(pcd.colors))
o3d.visualization.draw_geometries([pcd])