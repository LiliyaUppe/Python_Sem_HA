# 5'. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

import sympy
x = sympy.Symbol ('x')

y = 2*x**2 + 4*x + 5

c = 4*x**2 + 1*x + 4

# print(sympy.simplify(y+c))

with open('file1.txt', 'w') as data1:
    data1.write(f'{y}\n')

with open('file2.txt', 'w') as data2:
    data2.write(f'{c}\n')

with open('result.txt', 'w') as res:
    res.write(f'{sympy.simplify(y+c)}\n')

path = 'result.txt'
res = open(path, 'r')
for line in res:
     print(line)
res.close()
