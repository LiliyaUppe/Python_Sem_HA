# 2'. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

# vatiant1
number = int(input('Please, input N= '))
firstnumber = number
list = []  # пустой список,для хренеия множителей
i = 2  #first simple digit
while i <= number:
        if number % i == 0:
                list.append(i) 
                number //= i
        else:
                i += 1
if number > 1:
        list.append(number)
b = set(list)
print(f'list of simple digits {firstnumber}: {b}')

