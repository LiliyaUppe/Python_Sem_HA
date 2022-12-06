# 4'. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов многочлена 
# (значения от 0 до 100) и записать в файл многочлен степени k.(записать в строку)
# пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5

k = int(input('Please, imput k= '))
import random 
list = []
a = int(random.randint(0,100))
b = int(random.randint(0,100))
c = int(random.randint(0,100))
d = int(random.randint(0,100))
print(f'a = {a}, b = {b}, c = {c}, d = {d}')

from numpy import poly1d 
if k == 3:
    somePolynomial = poly1d([a,b,c,d])
    print(somePolynomial)
elif k == 2:
    somePolynomial = poly1d([a,b,c])
    print(somePolynomial)
elif k == 1:
    somePolynomial = poly1d([a,b])
    print(somePolynomial)
else:
    somePolynomial = poly1d([1,2,3])
    print('Sorry, k should be [1;3]. Try again!')

# with open('Polynomial.txt', 'r') as data:  # создает файл txt с индексами
#     data.write(f'{somePolynomial}')

with open('Polynomial.txt', 'w') as data:
    data.write(f'{somePolynomial}\n')
