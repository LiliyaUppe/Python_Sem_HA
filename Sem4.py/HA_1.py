# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  
 
#own variant
# import math
# pi = math.pi
# print(pi)

# d = (float(input('Please enter the d: ')))
# a = pi/d
# b = int(a)*d
# print(b)

#teacher

from math import pi

def format_by_mask(num: float, accuracy: float) -> float: # -> показывает какой тип данных возвращает функция и это ни на что не влияет
    """"форматирует число по заданной маске"""
    accuracy = str(accuracy)
    accuracy = len(accuracy[accuracy.find('.')+1::])
    return float(f'{pi:0.{accuracy}f}') # f'a:0.3f'

d = input('Введите точность в формате "0.001": ')
print(format_by_mask(pi, d))
