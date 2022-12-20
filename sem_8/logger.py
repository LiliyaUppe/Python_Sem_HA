# Модуль для записи резуьтатов вычислений

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('res_log.csv', 'a',  encoding='utf-8') as res_file:
        res_file.write(' Task: {}; Result: {}\n'.format(expr, result))
        

def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    history_file =  open('res_log.csv', 'r',  encoding='utf-8')
    a = history_file.read()
    history_file.close()
    return a




