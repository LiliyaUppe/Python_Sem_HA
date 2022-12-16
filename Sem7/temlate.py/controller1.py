# import game1
# import game2
import view
import logger
import random 




def run():
    i = 0
    while i<3:
        mode = view.choose_game()
        if mode == 'Noughts and crosses':
            print("Game №", i+1)
            # result = game1.run_game()
            result = random.randint(0,2)
            view.show_results(result)
            logger.log_result(i, result)
        if mode == 'Candy':
            print("Game №", i+1)
            # result = game2.run_game()
            result = random.randint(0,2)
            view.show_results(result)
            logger.log_result(i, result)
        i += 1



