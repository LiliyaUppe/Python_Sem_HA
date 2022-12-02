# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



a = input('Введите список чисел list: ').split(',')
list = [int(item) for item in a]
print(list)
multlist = []
# if len(list)%2 == 0:
for i in range (int(len(list)/2)+1):
    multlist.append(list[i]*list[(len(list)-i)-1])
print(multlist)

