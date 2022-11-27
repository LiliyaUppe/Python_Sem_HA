# 2'. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

# вариант мой
#запрос данных
x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))

#проверка истинности
def true_or_false(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    return result

#печать результата
if true_or_false(x, y, z) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

#вариант преподавателя
xp = [True, False]
yp = [True, False]
zp = [True, False]


for x in xp:
for y in yp:
for z in zp:
print(x, y, z)
res1 = not (x or y or z)
res2 = (not x) and (not y) and (not z)
print(res1 == res2)