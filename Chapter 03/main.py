from draw3d import *
from vectors import *
from math import sin, cos, pi

u = (1,-1,-1)
v = (0,0,2)
sub = subtract(v, u)
print(sub)
scaled = scale(.5, sub)
print(scaled)
final = add(scaled, u)
print(final)
            
# draw3d(
#         Arrow3D(*final)
        
#     )