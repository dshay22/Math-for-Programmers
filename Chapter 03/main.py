from draw3d import *

v = (-1,-2,2)
draw3d(
        Points3D(v),
        Arrow3D(v),
        Box3D(*v)
    )