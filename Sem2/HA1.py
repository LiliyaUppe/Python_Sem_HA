# 1. Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# variant_1
a = float(input('Введите вещественное число: '))
str_a = str(a)
str_a = str_a.replace('.', '')
lst_str = list(str_a)
lst_num = map(int, lst_str)
s = sum(lst_num)
print(s) 

# variant_2
a = float(input('Введите вещественное число: '))
str_a = str(a)
str_a = str_a.replace('.', '')
lst_str = list(str_a)
sum = 0
for str_a in lst_str:
    sum += int(str_a)
print(sum)