# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# vatiant1
number = int(input('Введите десятичное число n = '))
print(bin(number))


# vatiant2
number = int(input('Введите десятичное число n = '))
a = '' # пустой список,для хренеия остака от деления 
while number > 0:
    a = str(number % 2) + a 
    number = number // 2
print(f'0b{a}')