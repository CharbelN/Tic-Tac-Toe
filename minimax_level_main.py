import random
from minimax_level import UserPlay
from minimax_level import PcPlay
from minimax_level import GuessWinner
from minimax_level import Minimax
from  minimax_level import Maximize
from  minimax_level import print_board
 
 
array = [['', '', '', ''],
         ['', '', '', ''],
         ['', '', '', ''],
         ['', '', '', '']]
 
validaton = input("Do you want to start? yes/no\n")
 
user_f = ''
pc_f = ''
turn = 0

# if validaton == "yes":
#     user_f = 'X'
#     pc_f = '0'
#     turn = 0
# else:
#     user_f = '0'
#     pc_f = 'X'
#     turn = -1
 
# for i in range(0, 16):
#     if turn % 2 == 0:
#         UserPlay(array, user_f)
#     else:
#         alpha = -float('inf')
#         beta = float('inf')
#         array = Minimax(array, pc_f, user_f, 0, float('inf'),alpha,beta)
 
#     print_board(array)
 
#     var = GuessWinner(array, pc_f, user_f)
#     if var is not None:
#         if var == 1:
#             print("AI won")
#         elif var == -1:
#             print("Human won")
#         else:
#             print("It's a tie")
 
#     turn += 1



if validaton == "yes":
    user_f = 'X'
    pc_f = '0'
    turn = 0
else:
    user_f = '0'
    pc_f = 'X'
    turn = -1
 
for i in range(0, 16):
    if turn % 2 == 0:
        UserPlay(array, user_f)
    else:
        alpha = -float('inf')
        beta = float('inf')
        array = Minimax(array, pc_f, user_f, 0, 4 ,alpha,beta)
 
    print_board(array)
 
    var = GuessWinner(array, pc_f, user_f)
    if var is not None:
        if var == 1:
            print("AI won")
            break
        elif var == -1:
            print("Human won")
            break
        else:
            print("It's a tie")
 
    turn += 1
 

















#Easy: Call Minimax(array, pc_f, user_f, 0, 1) or max_depth = 2.
#Medium: Call Minimax(array, pc_f, user_f, 0, 2) or max_depth = 4.
#Hard: Call Minimax(array, pc_f, user_f, 0, float('inf')) for full depth.


#Easy Level: Depth 1 to 2

#The AI makes quick, shallow moves without much strategy. It only looks ahead one or two moves, making it easy to beat.
#Medium Level: Depth 3 to 5

#The AI looks ahead a few more moves, starting to employ some strategy. It becomes more challenging but still makes mistakes that a skilled player can exploit.
#Hard Level: Depth 6 to 9 (or full depth)

#The AI explores almost the entire game tree, making very strategic decisions. At this depth, it's much more difficult to beat, and it often plays optimally, aiming to either win or force a draw.


#Easy: Call Minimax(array, pc_f, user_f, 0, 1) or max_depth = 2.
#Medium: Call Minimax(array, pc_f, user_f, 0, 2) or max_depth = 4.
#Hard: Call Minimax(array, pc_f, user_f, 0, float('inf')) for full depth.


#Easy Level: Depth 1 to 2

#The AI makes quick, shallow moves without much strategy. It only looks ahead one or two moves, making it easy to beat.
#Medium Level: Depth 3 to 5

#The AI looks ahead a few more moves, starting to employ some strategy. It becomes more challenging but still makes mistakes that a skilled player can exploit.
#Hard Level: Depth 6 to 9 (or full depth)

#The AI explores almost the entire game tree, making very strategic decisions. At this depth, it's much more difficult to beat, and it often plays optimally, aiming to either win or force a draw.