import random


def print_board(array):
    for idx, row in enumerate(array):  # Loop directly through each row in the array with an index
        for j in range(3):  # Loop through each column in the row
            if row[j] == '':
                print("   ", end=' ')
            else:
                if row[j] == 'X':
                    print(' X ', end=' ')
                else:
                    print(' 0 ', end=' ')
            if j < 2:
                print("|", end=' ')
        print('') 
        if idx < 2:
            print("---------------")




def UserPlay(array,user_f):
    while (True):
        user = input("choice:")
        if (array[int(user[0])][int(user[2])] == ''):
            array[int(user[0])][int(user[2])] = user_f
            print("")
            break


def PcPlay(array, pc_f, user_f, human_style='aggressive'):
    best_move = expectimax_with_probabilities(array, pc_f, user_f, is_ai_turn=True, human_style=human_style)
    if isinstance(best_move, tuple):
        array[best_move[0]][best_move[1]] = pc_f
    print_board(array)
    print("")

    

def GuessWinner(array,pc_f,user_f):

    if array[0][0] == array[0][1] == array[0][2] == pc_f or array[1][0] == array[1][1] == array[1][2] ==pc_f or \
            array[2][0] == array[2][1] == array[2][2] == pc_f or array[0][0] == array[1][0] == array[2][0] == pc_f or\
            array[0][1] == array[1][1] == array[2][1] == pc_f or array[0][2] == array[1][2] == array[2][2] == pc_f or \
            array[0][0] == array[1][1] == array[2][2] == pc_f or array[0][2] == array[1][1] == array[2][0] == pc_f:
        return 1
    if array[0][0] == array[0][1] == array[0][2] == user_f or array[1][0] == array[1][1] == array[1][2] == user_f or \
            array[2][0] == array[2][1] == array[2][2] == user_f or array[0][0] == array[1][0] == array[2][0] == user_f or\
            array[0][1] == array[1][1] == array[2][1] == user_f or array[0][2] == array[1][2] == array[2][2] == user_f or \
            array[0][0] == array[1][1] == array[2][2] == user_f or array[0][2] == array[1][1] == array[2][0] == user_f:
        return -1

    for i in range(3):
        for j in range(3):
            if array[i][j] == '':
                return None
    return 0


def actions(state):
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == '':
                possible_moves.append((i, j))
    return possible_moves


def expectimax(array, pc_f, user_f, is_ai_turn=True, top_level=True):
    winner_status = GuessWinner(array, pc_f, user_f)
    if winner_status is not None:
        return winner_status  

    if is_ai_turn:
        best_value = -float('inf')
        best_action = None
        for i in range(3):
            for j in range(3):
                if array[i][j] == '':
                    array[i][j] = pc_f
                    print(f"AI trying move at ({i}, {j})")
                    value = expectimax(array, pc_f, user_f, False, top_level=False)
                    
                    array[i][j] = ''
                    
                    if value > best_value:
                        best_value = value
                        best_action = (i, j)
                    
        return best_action if top_level else best_value

    else:
        expected_value = 0
        possible_moves = actions(array)
        probability = 1 / len(possible_moves) if possible_moves else 0
    
        
        for i, j in possible_moves:
            array[i][j] = user_f
            
            value = expectimax(array, pc_f, user_f, True, top_level=False)
            
            array[i][j] = ''
            
            expected_value += probability * value
        
        return expected_value





def expectimax_with_probabilities(array, pc_f, user_f, is_ai_turn=True, top_level=True, human_style='defensive'):
    winner_status = GuessWinner(array, pc_f, user_f)
    if winner_status is not None:
        return winner_status

    if is_ai_turn:
        best_value = -float('inf')
        best_action = None
        for i in range(3):
            for j in range(3):
                if array[i][j] == '':
                    array[i][j] = pc_f
                    value = expectimax_with_probabilities(array, pc_f, user_f, False, top_level=False, human_style=human_style)
                    array[i][j] = ''
                    
                    if value > best_value:
                        best_value = value
                        best_action = (i, j)
        return best_action if top_level else best_value
    else:
        possible_moves = actions(array)
        
        move_probabilities = calculate_move_probabilities(array, possible_moves, pc_f, user_f, human_style)

        expected_value = 0
        for i, j in possible_moves:
            probability = move_probabilities.get((i, j), 0)
            array[i][j] = user_f
            value = expectimax_with_probabilities(array, pc_f, user_f, True, top_level=False, human_style=human_style)
            array[i][j] = ''
            
            expected_value += probability * value
        return expected_value
    
    

def calculate_move_probabilities(array, possible_moves, pc_f, user_f, human_style):
    move_probabilities = {}
    
    if human_style == 'defensive':
        for i, j in possible_moves:
            array[i][j] = user_f
            if GuessWinner(array, user_f, pc_f) == 1: 
                move_probabilities[(i, j)] = 0.9
            else:
                move_probabilities[(i, j)] = 0.1
            array[i][j] = ''
    elif human_style == 'aggressive':
        for i, j in possible_moves:
            array[i][j] = user_f
            if GuessWinner(array, user_f, pc_f) == -1: 
                move_probabilities[(i, j)] = 0.9 
            else:
                move_probabilities[(i, j)] = 0.1 
            array[i][j] = ''

    total_prob = sum(move_probabilities.values())
    if total_prob > 0:
        move_probabilities = {move: prob / total_prob for move, prob in move_probabilities.items()}

    return move_probabilities