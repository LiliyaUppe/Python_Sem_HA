def choose_game():
    print('Input "1" for "Noughts and crosses"')
    print('Input "2" for "Candy"')
    x = int(input('Choose the game: '))
    if 0 < x and x < 3:
        if x == 1:
            mode = 'Noughts and crosses'
            print('Your choise is "Noughts and crosses"')
        elif x == 2:
            mode = 'Candy'
            print('Your choise is "Candy"')
        else:
            print('Choose "1" or "2"')
        return mode



def show_results(result):
    if result == 1:
        print('Winner is 1')
    elif result == 2:
        print('Winner is 2')
    elif result == 0:
        print('You are friends')
    else:
        print('Error')
    print (result)


