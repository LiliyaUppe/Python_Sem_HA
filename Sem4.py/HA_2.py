# 2'. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

# vatiant1
# number = int(input('Please, input N= '))
# firstnumber = number
# list = []  # пустой список,для хренеия множителей
# i = 2  #first simple digit
# while i <= number:
#         if number % i == 0:
#                 list.append(i) 
#                 number //= i
#         else:
#                 i += 1
# if number > 1:
#         list.append(number)
# b = set(list)
# print(f'list of simple digits {firstnumber}: {b}')

#teacher

def dividers(a: int, uniq: bool = False) -> list[int]:
        """"Возвращает список простых делителей числа.
        uniq = True вернет список уникальных делителей"""
        i = 2
        dividers = []
        while a != 1:
                while a % i == 0:
                        dividers.append(i)
                        a //= i
                i += 1
        if uniq:
                return list(set(dividers))
        else:
                return dividers


a = 81
print(f'Список натуральных делителей числа {a}:{dividers(a)}')
print(f'Список уникальных делителей числа {a}:{dividers(a, True)}')