# 1'. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


data = [2, 3, 5, 9, 3]
index = data[1::2]
print(index)
sum = sum(index)
print(sum)
