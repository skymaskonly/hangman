from random import choice

word_list = ['пальма', 'мир', 'волк', 'вагнер', 'сомали',
            'хардкор', 'милитари', 'офис', 'центр', 'ак']

def hangman(word):
    wrong = 0
    stages = ['',
             '______      ',
             '|           ',
             '|     |     ',
             '|     0     ',
             '|    /|\    ',
             '|    / \    ',
             '|           '
             ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Добро пожаловать на казнь!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Введите букву: '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print('\n'.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: {}.'.format(word))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('Вы проиграли! Было загадано слово: {}.'.format(word))

hangman(choice(word_list))