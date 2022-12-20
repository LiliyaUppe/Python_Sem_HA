# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# variant_own
a = input('Введите список чисел list: ').split(',')
list = [int(item) for item in a]
print(list)
multlist = []
# if len(list)%2 == 0:
for i in range (int(len(list)+1)//2):  
    multlist.append(list[i]*list[(len(list)-i)-1])
print(multlist)

#teacher

# def pair_multi(nums: list[int] -> list[int]):
#     """return list of multiply pair"""
#     pairs = []
#     iterations = int((len(nums)+1)//2)
#     print(iterations)
#     for i in range(iterations):
#         pairs.append(nums[i]*nums[len(nums)-1-i])
#     return pairs

# nums = [2, 3, 4 ,5 ,6]
# print(pair_multi(nums))