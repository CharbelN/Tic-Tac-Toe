import random

from alpha_beta import UserPlay
from alpha_beta import PcPlay
from alpha_beta import GuessWinner
from alpha_beta import Minimax
from alpha_beta import Maximize
from alpha_beta import print_board




array = [['', '', '', ''],
         ['', '', '', ''],
         ['', '', '', ''],
         ['', '', '', '']]



validaton = input("Do you want to start? yes/no\n")

user_f = ''
pc_f = ''

turn = 0
if(validaton == "yes"):
    user_f = 'X'
    pc_f = '0'
    turn = 0
else:
    user_f = '0'
    pc_f = 'X'
    turn = -1



for i in range(0,16):

    if turn % 2 == 0:
        UserPlay(array, user_f)
    else:
        alpha = -float('inf')
        beta = float('inf')
        array = Minimax(array, pc_f, user_f,alpha, beta)

    print_board(array)

    var = GuessWinner(array, pc_f, user_f)
    if var is not None:
        if var == 1:
            print("AI won")
        elif var == -1:
            print("Human won")
        else:
            print("tie")

    turn += 1



