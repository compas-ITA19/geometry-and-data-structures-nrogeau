from compas.geometry import Vector
from compas.geometry import Polygon

a = [1, 0, 0]
b = [0, 1, 0]
c = [-1, 0, 0]

polygon = Polygon([a, b, c])

def get_area(polygon):

    center = polygon.center
    Atot = 0
    points = polygon.points
    points.append(points[0])

    for i in range(len(points)-1):
        u = Vector.from_start_end(points[i], points[i+1])
        v = Vector.from_start_end(points[i], center)
        uxv = u.cross(v)
        Atot += uxv.length/2
    
    return Atot

print(get_area(polygon))