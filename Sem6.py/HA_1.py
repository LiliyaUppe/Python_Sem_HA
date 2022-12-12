#4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


number = input('введите номер четверти: ')
dictionary =\
     {
        '1':'x ∈ (0; +∞) y ∈ (0; +∞)', 
        '2':'x ∈ (-∞; 0) y ∈ (0; +∞)', 
        '3':'x ∈ (-∞; 0) y ∈ (-∞; 0)', 
        '4':'x ∈ (0; +∞) y ∈ (-∞; 0)'
    } 

print(dictionary[number])


#lecture_3
# def f(x):
#     return x**3

# list = []
# for i in range (1,21):
#     if (i%2==0):
#         list.append(f(i))
#         print(list)

# list = [(i,f(i)) for i in range(1,21) if i%2==0]
# print(list)