import os
import compas

from compas.datastructures import Mesh
from compas.topology import breadth_first_ordering
from compas.utilities import i_to_red
from compas_plotters import MeshPlotter
from compas_plotters import Plotter

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

def traverse_mesh(mesh, start):

    vertices=[start]
    edges=[]
    faces=[mesh.vertex_faces(vertices[0])[0]]
    
    for i in range(100):
        try:
            next_vertice = mesh.face_vertex_descendant(faces[i], vertices[i])
            next_next_vertice = mesh.face_vertex_descendant(faces[i], next_vertice)
            
            neighbour_faces = mesh.edge_faces(next_vertice, next_next_vertice)
            if faces[i] == neighbour_faces[0]: next_face = neighbour_faces[1]
            else : next_face = neighbour_faces[0]
            
            vertices.append(next_vertice)
            edges.append((vertices[i], next_vertice))
            faces.append(next_face)
            
        except: break
    return edges

#traverse the mesh starting from a specified boundary vertice
edges = traverse_mesh(mesh, 1)

#traverse the mesh starting from each boundary vertice (resulting in a grid)
"""
edges=[]
for i in mesh.boundaries()[0]:
    edges += traverse_mesh(mesh, i)
"""

#base mesh
all_edges = mesh.edges()

# vizualisation part

def draw_edges_on_plotter(edges, color):

    for i in edges:

        lines.append({'start': mesh.vertex_coordinates(i[0]), 'end': mesh.vertex_coordinates(i[1]), 'color': color,'width': 1})

        pts.append({

        'pos': mesh.vertex_coordinates(i[0]), 

        'radius': 0.01, 

        'edgecolor': (255,0,0), 

        'facecolor': (255,255,0)})

plotter = Plotter(figsize=(16, 10))
lines = []
pts = []
draw_edges_on_plotter(all_edges, (0, 0, 255))
draw_edges_on_plotter(edges, (0, 255, 0))
plotter.draw_points(pts)
plotter.draw_lines(lines)
plotter.show()