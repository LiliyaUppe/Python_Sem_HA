# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python(дополнительный sympy,scipy)

# variant1
# a = float(input('A= '))
# b = float(input('B= '))
# c = float(input('C= '))
# print (f'{a}*x**2 + {b}*x + {c} = 0')

# import math
# d = b**2 - 4*a*c
# print(d)
# if d > 0:
#     x1 = ((-b+math.sqrt(d)))/2*a
#     x2 = ((-b-math.sqrt(d)))/2*a
#     print(x1, x2)
# elif d == 0:
#     x1 = -b/(2*a)
#     print(x1)
# else:
#     print('нет действительных корней')

# variant2_sympy важная в анализе дат
import sympy
x = sympy.Symbol('x')
a = input('input eq: ') #eq - уравнение
print(sympy.solve(a,x)) #метод слолв возвращает список корней
