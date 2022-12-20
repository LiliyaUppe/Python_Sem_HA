# Модуль для ввода/вывода информации

def choose() -> str:
    """"Выбор режима работы приложения"""
    print('Input "1" for "calculus"')
    print('Input "2" for "solve an equation"')
    print('Input "3" for "simpify a polynomial"')
    print('Input "4" for "history"')
    x = int(input('Choose the mode: '))
    if 0 < x and x < 5:
        if x == 1:
            mode = 'execute_expr'
            print('Your choise is "Calculus"')
        elif x == 2:
            mode = 'solve_eq'
            print('Your choise is "Solve an equation"')
        elif x == 3:
            mode = 'simpify_pol'
            print('Your choise is "Simpify a polynomial"')
        elif x == 4:
            mode = 'get_history'
            print('Your choise is "History"')
        else:
            print('Incorrect input')
        return mode


def get_expr() -> str:
    """"Запрашивает у пользователя задачу"""
    expr = input('Input an equation: ')
    return expr


def show_res(result: str):
    """Выводит результат"""
    print(f'result: {result}')


def erorr_mode():
    """Выводит сообщение об ошибке выбора режима"""
    print('Incorrect input')  


def show_history(history: str):
    """Выводит истроию оперций"""
    print(history)
