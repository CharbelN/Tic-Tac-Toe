from expectimax import expectimax
from expectimax import print_board
from expectimax import GuessWinner
from expectimax import UserPlay
from expectimax import PcPlay

array = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

validaton = input("Do you want to start? yes/no\n")

user_f = ''
pc_f = ''
is_ai_turn = False  

if validaton.lower() == "yes":
    user_f = 'X'
    pc_f = '0'
    is_ai_turn = False  
else:
    user_f = '0'
    pc_f = 'X'
    is_ai_turn = True 




for i in range(9):
    if not is_ai_turn:  
        UserPlay(array, user_f)
    else:  
        PcPlay(array, pc_f, user_f, human_style='aggressive') 

    print_board(array)

    var = GuessWinner(array, pc_f, user_f)
    if var is not None:
        if var == 1:
            print("AI won")
        elif var == -1:
            print("Human won")
        else:
            print("Tie")
        break  

    is_ai_turn = not is_ai_turn