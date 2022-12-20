import view
import model
import logger

# Реализовать калькулятор с системой логирования:
# 1) решение вводимых примеров (2+3) -> 5 ; 2**3 + (3+6)/(1+2) ->  11
# 2) решение уравнений (x+3 = 0) -> -3
# 3) упрощение многочленов (x*2 + 3*x2 + 4) -> 4*x*2 + 4

# Записать в файл "задачу" от пользователя и ответ.


def run_calc():
    mode = view.choose()
    if mode == 'execute_expr':
        expr = view.get_expr()
        result = model.execute_expr(expr)
        view.show_res(result)
        logger.log_exec(expr, result)
    elif mode == 'solve_eq':
        expr = view.get_expr()
        result = model.solve_eq(expr)
        view.show_res(result)
        logger.log_exec(expr, result)
    elif mode == 'simpify_pol':
        expr = view.get_expr()
        result = model.simpify_pol(expr)
        view.show_res(result)
        logger.log_exec(expr, result)
    elif mode == 'get_history':
        history = logger.get_history()
        view.show_history(history)
    else:
        view.erorr_mode()
