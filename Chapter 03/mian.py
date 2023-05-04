from draw3d import *
from draw2d import *
from vectors import *
from math import sin, cos, pi

top = (0,0,1)
bottom = (0,0,-1)
xy_plane = [(1,0,0), (0,1,0), (-1,0,0), (0,-1,0)]
edges = [Segment3D(top,p) for p in xy_plane] +\
            [Segment3D(bottom, p) for p in xy_plane] +\
            [Segment3D(xy_plane[i], xy_plane[(i + 1) % 4]) for i in range(0,4)]
            
draw3d(*edges)