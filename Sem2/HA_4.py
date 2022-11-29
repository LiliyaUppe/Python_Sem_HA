# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2


def get_numers(n):  # создаем список от -n до n
    lst = []
    for i in range(-n, n + 1, 1):
        lst.append(i)
    return lst


with open('file.txt', 'w') as data:  # создает файл txt с индексами
    data.write('0\n')
    data.write('1\n')
    

def get_num_from_txt(path):  # переводим индексы из файла в список
    data = open(path, 'r')
    numlist = [int(line.strip()) for line in data]
    data.close()
    return numlist

def mult_index (numbers, numlist):
    mult = 1
    for i in numlist:
        mult *= numbers[i]
    return mult

n = int(input('Введите число N: '))
numbers = get_numers(n)
path = 'file.txt'
numlist = get_num_from_txt(path)

print(f'Список от -N до N: {numbers}')
print(f'Индексы из файла txt: {numlist}')
print(f'Произведение элементов: {mult_index(numbers,numlist)}')