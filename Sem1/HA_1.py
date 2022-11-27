#1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> не

#my variant
# dayOfWeek = int(input('d = '))
# if dayOfWeek in range (1,6):
#   print ('no, it isn't')
# elif dayOfWeek == 6 or dayOfWeek == 7:
#     print('yes, it is')
# else:
#     print('please, try again!')

# teacher variant by dictionary

workday = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thurthday', 5: 'Fri'}
weekend = {6: 'Sarturday', 7: 'Sunday'}
while True:
  a = int(input())
  if a >= 6 and a <= 7:
    print('Weekend')
    print(f'This is {weekend[a]}')
    break
  elif a > 0 and a <= 5:
    print('Workday')
    print(f'This is {workday[a]}')
    break
  else:
    print('Error')