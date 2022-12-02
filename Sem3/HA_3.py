# 3'. Задайте список из вещественных чисел. 
# Hапишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (максимальное значение у числа 1.2 , минимальное у 10.01)

# вариант_1(только для float по условию)

def get_fractional_part(list): # метод получения списка десятой части элементов
    for i in range(len(list)):
        list[i] = round(list[i] % 1, 2)
    return list

def diff_max_min(list): # вычисление max и min
    max = list[0]
    min = list[0]
    for i in range(len(list)):
        if list[i] != 0: # условие добавлено для игнорирования дробной части целого числа, т.е 0
            if list[i] > max:
                max = list[i]
            elif list[i] < min:
                min = list[i]
    return (max-min)

float_list = [1.1, 1.2, 3.1, 5, 10.01]

print(f' {float_list} => {diff_max_min(get_fractional_part(float_list))}')


# variant2 (для дробных и целых чисел включительно)
# a = input('Введите список чисел list: ').split(',')
# list = [float(item) for item in a]
# print(list)
# listsplit = []
# for i in range (len(list)): 
#    listsplit.append(list[i]-int(list[i]))
# print (listsplit)
# print(max(listsplit), '-', min(listsplit), '=', max(listsplit)-min(listsplit))