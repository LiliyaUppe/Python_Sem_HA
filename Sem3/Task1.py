import os
os.system('cls||clear')
#Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке некое число.
# Пример:
# ['114411', 'sjngsjgng', '123fsghs'] -> No
# ['12', 12] -> Yes

# задача сводиться к проверке типу данных int, float, char, string
# тип данных элементов определяется через вызов ф-ции type(element) некого элемента
# a = 5
# print(type(a))


# list = ['114411', 'sjngsjgng', '123fsghs']
# list = [5, 12]
# for i in range (len(list)):
#     if type(list[i]) == 'int' or type(list[i]) == 'float':
#         print('There is an element', i, 'like digit')
#     else:
#          print("There isn't an element", i, "like digit")

# variant2
mass = ['ssss', 'sdfsdf', '33']
types = [str(type(i)) for i in mass]
print(types)
if "<class 'int'>" in types or "<class 'float'>" in types:
    print('Yes')
else:
    print('No')
