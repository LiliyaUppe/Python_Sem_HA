# Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# *' 4 5 -> 20
# *' 6 3 -> 6
# *' 7 11 -> 77
# *' 6 8 -> 24

# varian1
def least_common_multiple (a,b):
    # selecting the greater number 
    if a > b: 
        greater = a 
    else: 
        greater = b 
    while(True): 
        if((greater % a== 0) and(greater % b == 0)): 
            lcm = greater 
            break 
        greater += 1 
    return lcm

a = float(input('a = '))
b = float(input('b = '))
print(f'lcm ({a}, {b})= {least_common_multiple(a, b)}')


