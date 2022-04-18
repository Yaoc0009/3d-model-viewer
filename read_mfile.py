import open3d as o3d
import numpy as np

filename = 'assets/gargoyle.txt'
with open(filename, 'r') as f:
    lines = f.readlines()

v = []
v_normal = []
f = []

for line in lines:
    line_split = line.strip().split()
    if line_split[0] == 'Vertex':
        v.append([float(line_split[2]), float(line_split[3]), float(line_split[4])])
        v_normal.append([float(line_split[5].split('(')[-1]), float(line_split[6]), float(line_split[7].split(')')[0])])
    elif line_split[0] == 'Face':
        f.append([int(line_split[2]), int(line_split[3]), int(line_split[4])])

v = np.array(v)
f = np.array(f) - 1
print("Number of Vertices: ", len(v))
print("Number of Faces: ", len(f))

mesh = o3d.geometry.TriangleMesh()
mesh.vertices = o3d.utility.Vector3dVector(v)
mesh.triangles = o3d.utility.Vector3iVector(f)
mesh.paint_uniform_color([1, 0.706, 0])
mesh.compute_vertex_normals()
print(mesh)
o3d.visualization.draw_geometries([mesh])