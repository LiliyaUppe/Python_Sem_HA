#4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# my variant
# a = int(input('введите номер четверти: '))
# if (a==1):
#     print('x ∈ (0; +∞)')
#     print('y ∈ (0; +∞)')
# elif (a==2):
#     print('x ∈ (-∞; 0)') 
#     print('y ∈ (0; +∞)')
# elif (a==3):
#    print('x ∈ (-∞; 0)')
#    print('y ∈ (-∞; 0)')
# elif (a==4):
#    print('x ∈ (0; +∞)')
#    print('y ∈ (-∞; 0)')

# teacher variant
# dictionary method
a = input()
d = {'1':'x>0 y>0', '2': 'x<0 y>0', '3': 'x<0 y<0', '4': 'x>0 y<0'} 
#словарь содержит в фигурных скобках ключи '1','2' а принт распечатывает эти ключи в соответсвии с введенными данными
print(d[a])