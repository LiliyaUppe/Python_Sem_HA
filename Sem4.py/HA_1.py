# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  
 

import math
pi = math.pi
print(pi)

d = (float(input('Please enter the d: ')))
a = pi/d
b = int(a)*d
print(b)

