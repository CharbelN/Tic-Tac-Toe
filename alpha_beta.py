import random
import sys


 
def print_board(array):
    for idx, row in enumerate(array):  
        for j in range(4):  
            if row[j] == '':
                print("   ", end=' ')
            else:
                if row[j] == 'X':
                    print(' X ', end=' ')
                else:
                    print(' 0 ', end=' ')
            if j < 3:
                print("|", end=' ')
        print('')  
        if idx < 3:  
            print("---------------------")




def UserPlay(array,user_f):
    while (True):
        user = input("choice:")
        if (array[int(user[0])][int(user[2])] == ''):
            array[int(user[0])][int(user[2])] = user_f
            print("")
            break

def PcPlay(array):
    while (True):
        x = random.randrange(0, 4)
        y = random.randrange(0, 4)
        if (array[int(x)][int(y)] == ''):
            array[int(x)][int(y)] = '0'
            print_board(array)
            print("")
            break

def GuessWinner(array, pc_f, user_f):
    # Check rows and columns
    for i in range(4):
        if array[i][0] == array[i][1] == array[i][2] == array[i][3] != '':
            return 1 if array[i][0] == pc_f else -1
        if array[0][i] == array[1][i] == array[2][i] == array[3][i] != '':
            return 1 if array[0][i] == pc_f else -1
 
    # Check diagonals
    if array[0][0] == array[1][1] == array[2][2] == array[3][3] != '':
        return 1 if array[0][0] == pc_f else -1
    if array[0][3] == array[1][2] == array[2][1] == array[3][0] != '':
        return 1 if array[0][3] == pc_f else -1
 
    for i in range(4):
        for j in range(4):
            if array[i][j] == '':
                return None  # Game is still ongoing
 
    return 0  # It's a tie



def Minimax(array, pc_f, user_f,alpha, beta):

    nodes_explored = [0]
    current_depth = 0
    max_depth = [0]
    max_depth[0] = max(max_depth[0], current_depth)

    v = -100
    coordonne = ()

    winner = GuessWinner(array, pc_f, user_f)
    if winner is not None:
        return winner

    for i in range(4):
        for j in range(4):
            if array[i][j] == '':
                array[i][j] = pc_f
                score = Minimize(array, pc_f, user_f, nodes_explored, current_depth + 1, max_depth,alpha, beta)
                if score > v:
                    coordonne = (i, j)
                    v = score
                array[i][j] = ''
                alpha = max(alpha, v)
                if beta <= alpha:  # Prune the branch
                    break

    print("nodes explore: " + str(nodes_explored))
    print("depht: " + str(max_depth[0]))

    if coordonne:
        array[coordonne[0]][coordonne[1]] = pc_f
    return array


def Maximize(array, pc_f, user_f, nodes_explored, current_depth, max_depth,alpha, beta):

    var = GuessWinner(array, pc_f, user_f)
    if var is not None:
        return var

    v = -100
    nodes_explored[0] += 1
    max_depth[0] = max(max_depth[0], current_depth)

    for i in range(4):
        for j in range(4):
            if array[i][j] == '':
                array[i][j] = pc_f
                score = Minimize(array, pc_f, user_f, nodes_explored, current_depth + 1, max_depth,alpha, beta)
                v = max(v, score)
                array[i][j] = ''
                alpha = max(alpha, v)
                if beta <= alpha:  # Prune the branch
                    break
    return v


def Minimize(array, pc_f, user_f, nodes_explored, current_depth, max_depth,alpha, beta):

    var = GuessWinner(array, pc_f, user_f)
    if var is not None:
        return var

    v = 100
    nodes_explored[0] += 1
    max_depth[0] = max(max_depth[0], current_depth)

    for i in range(4):
        for j in range(4):
            if array[i][j] == '':
                array[i][j] = user_f
                score = Maximize(array, pc_f, user_f, nodes_explored, current_depth + 1, max_depth,alpha, beta)
                v = min(v, score)
                array[i][j] = ''
                beta = min(beta, v)
                if beta <= alpha:  # Prune the branch
                    break
    return v