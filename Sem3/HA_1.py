# 1'. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# variant_own
list = [2, 3, 5, 9, 3]
newlist = []
for i in range(len(list)):
    if i % 2 != 0:
        newlist.append(list[i])
    print(newlist)
else:
    -1
sum = sum(newlist)
print(sum)

# teacher
def sum_of_even(nums: list[int]) -> int:
    """ Return sum of even indexes"""
    return sum(nums[1::2]) # в [] указывается срез c 1 элемента через шаг=2 в списке nums

a = [2, 3, 5, 9, 3]
print(a[1::2])
print(sum_of_even(a))
