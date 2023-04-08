import sys
import math
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon, FancyArrowPatch

sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 03' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 04' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 05' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 06' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 07' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 09' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 10' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 11' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 12' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 13' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 14' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 15' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 16' )
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 08' )
from  vector_drawing import *
from vectors import *
from colors import *
from draw2d import *


if __name__ == '__main__':
    print('matplotlib: {}'.format(matplotlib.__version__))
    v = (-1,-2,2)
    draw3d(
        Points3D(v),
        tempt(v),
        Box3D(*v)
    )
