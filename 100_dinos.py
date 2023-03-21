import sys
import math
sys.path.insert(1,'C:\\Users\\doria\\Documents\\GitHub\School-Work\\Python Fun\\Primes Spiral\\math-for-programmers\\Math-for-Programmers\\Chapter 02' )
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

def one_hundred_dinos(dino_vec, scalarX, scalarY):
    
    dino_list = []
    for i in range(scalarX):
        for j in range(scalarY):
            dino_list.append([add((11*i, 11*j), v) for v in dino_vec])
    
    allDinos = []
    for z in dino_list:
        allDinos.append(Polygon(*z))
    
    draw(
        *allDinos,
        grid=None,
        axes=None,
        origin=None
    )
    
    return allDinos
    
    
if __name__ == '__main__':
    dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
    ]
    
    one_hundred_dinos(dino_vectors, 10, 10)