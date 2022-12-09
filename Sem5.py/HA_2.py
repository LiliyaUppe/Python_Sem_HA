
#поле для игры
def show_field():
    global field
    for i in range(0, len(field), 3):
        print(field[i], field[i+1], field[i+2])

field = [0, 1, 2, 3, 4, 5, 6, 7, 8]
show_field()

#выберите номер клеточки есть готовые функции для бота
