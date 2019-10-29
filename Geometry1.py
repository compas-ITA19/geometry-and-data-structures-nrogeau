from compas.geometry import Vector

u = Vector(0, 2, 3)
v = Vector(4, 5, 7)

def get_orthonormal_frame(u,v):

    # Orthogonal frame
    a = Vector.cross(u,v)
    b = Vector.cross(a,u)
    c = Vector.cross(a,b)

    # Normalized frame
    a.unitize()
    b.unitize()
    c.unitize()

    return (a,b,c)

print(get_orthonormal_frame(u, v))