def log_result(i, result):
    with open('log.csv', 'a') as file:
        file.write('Game:{};Winner:{}\n'.format(i, result))
    return 'result is written'
