# Задача 2.

# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))

# Ввод:
# house=дом car=машина men=человек tree=дерево
# Вывод:
# (('house', 'дом'), ('car', 'машина'), ('men', 'человек'), ('tree', 'дерево'))

# dictionary = \
#     {
#     'house': 'дом', 
#     'car': 'машина', 
#     'men': 'человек',  
#     'tree': 'дерево'
#     }
# print(list(map(tuple,dictionary.items())))

#variant own
t = 'house=дом car=машина men=человек tree=дерево'
t2 = t.replace('=', ':')
print(t2)
a = t2.split(' ')
print(a)
tpl = tuple(a)
print(type(tpl))
print(tpl)

#teacher

# a = 'house=дом car=машина men=человек tree=дерево'.split()
# a = tuple(map(lambda x: tuple(x.split('=')),a))
# print(a)