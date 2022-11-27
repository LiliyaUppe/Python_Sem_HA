#4. напишите программу, которая будет на вход принимат число N
# и выводить чтсла от -N до N

# #варант1_вывод в стлбик
# n = int(input('N = '))
# for i in range(-n,n+1):
#      print(i) 

# #варант2_вывод в строку через запятую
# n = int(input('N = '))
# for i in range(-n,n+1):
#     print(i, end = ',') 

#варант3_вывод в строку как массив
# n = int(input('N = '))
# a = []
# for i in range(-n,n+1):
#     a.append(i) #.append добавляет элемент в конц списка
#     print(f'{i}', end = ' ')
# print()
# print(a)     

#варант4_вывод в строку как массив
# n = int(input('N = '))
# a = []
# b = ' '
# for i in range(-n,n+1):
#     a.append(i) 
#     b+= f' {i}'    
# print(b)
