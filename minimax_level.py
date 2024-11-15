import random
 
 
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
 
 
def UserPlay(array, user_f):
    while True:
        user = input("choice (e.g., 0 1):")
        if array[int(user[0])][int(user[2])] == '':
            array[int(user[0])][int(user[2])] = user_f
            print("")
            break
 
 
def PcPlay(array):
    while True:
        x = random.randrange(0, 4)
        y = random.randrange(0, 4)
        if array[int(x)][int(y)] == '':
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
 
 
def Minimax(array, pc_f, user_f, depth, max_depth,alpha, beta):
    nodes_explored = [0]
    current_depth = 1
    final_depth = [0]
 
    v = -100
    coordonne = ()
    for i in range(4):
        for j in range(4):
            if array[i][j] == '':
                array[i][j] = pc_f
                score = Minimize(array, pc_f, user_f, depth + 1, max_depth, nodes_explored, current_depth + 1,final_depth,alpha, beta)
                if score > v:
                    coordonne = (i, j)
                    v = score
                array[i][j] = ''
                alpha = max(alpha, v)
                if beta <= alpha:  # Prune the branch
                    break
    array[coordonne[0]][coordonne[1]] = pc_f
 
    print("nodes explored: " + str(nodes_explored[0]))
    print("depth reached: " + str(final_depth[0]))
 
    return array
 
 
def Maximize(array, pc_f, user_f, depth, max_depth, nodes_explored, current_depth,final_depth,alpha, beta):
    if depth == max_depth:
        return evaluate_boardeasy(array, pc_f, user_f)
 
    var = GuessWinner(array, pc_f, user_f)
    if var is not None:
        return var
 
    nodes_explored[0] += 1
    final_depth[0] = max(final_depth[0], current_depth)
    v = -100
 
    for i in range(4):
        for j in range(4):
            if array[i][j] == '':
                array[i][j] = pc_f
                score = Minimize(array, pc_f, user_f, depth + 1, max_depth, nodes_explored, current_depth + 1,final_depth,alpha,beta)
                v = max(v, score)
                array[i][j] = ''
                alpha = max(alpha, v)
                if beta <= alpha:  # Prune the branch
                    break
   
    return v
 
 
 
def Minimize(array, pc_f, user_f, depth, max_depth, nodes_explored, current_depth,final_depth,alpha, beta):
    if depth >= max_depth:
        return evaluate_boardeasy(array, pc_f, user_f)
 
    var = GuessWinner(array, pc_f, user_f)
    if var is not None:
        return var
 
    nodes_explored[0] += 1
    final_depth[0] = max(final_depth[0], current_depth)
    v = 100
 
    for i in range(4):
        for j in range(4):
            if array[i][j] == '':
                array[i][j] = user_f
                score = Maximize(array, pc_f, user_f, depth + 1, max_depth, nodes_explored, current_depth + 1,final_depth,alpha,beta)
                v = min(v, score)
                array[i][j] = ''
                beta = min(beta, v)
                if beta <= alpha:  # Prune the branch
                    break

    return v




def evaluate_boardmedium(array, pc_f, user_f):
    score = 0

    # Helper function to evaluate sequences in a given line (row, column, or diagonal)
    def evaluate_line(line, pc_f, user_f):
        pc_count = line.count(pc_f)  # Count pc's pieces in the line
        user_count = line.count(user_f)  # Count user's pieces in the line
        empty_count = line.count('')  # Count empty spaces

        # Case: Line is winnable for the PC
        if user_count == 0:
            if pc_count == 4:
                return 100  # PC wins
            elif pc_count == 3 and empty_count == 1:
                return 50  # PC is 1 move away from winning
            elif pc_count == 2 and empty_count == 2:
                return 10  # PC has potential to win
            elif pc_count == 1 and empty_count == 3:
                return 1  # Weak potential for PC

        # Case: Line is winnable for the user
        if pc_count == 0:
            if user_count == 4:
                return -100  # User wins
            elif user_count == 3 and empty_count == 1:
                return -50  # User is 1 move away from winning
            elif user_count == 2 and empty_count == 2:
                return -10  # User has potential to win
            elif user_count == 1 and empty_count == 3:
                return -1  # Weak potential for User

        # Case: Line is contested, no clear advantage
        return 0

    # Evaluate rows and columns
    for i in range(4):
        # Evaluate rows
        score += evaluate_line(array[i], pc_f, user_f)  # Full row

        # Evaluate columns
        score += evaluate_line([array[j][i] for j in range(4)], pc_f, user_f)  # Full column

    # Evaluate diagonals
    score += evaluate_line([array[i][i] for i in range(4)], pc_f, user_f)  # Main diagonal
    score += evaluate_line([array[i][3-i] for i in range(4)], pc_f, user_f)  # Anti-diagonal

    return score

 
def evaluate_boardeasy(array, pc_f, user_f):
    score = 0

    # Helper function to evaluate sequences in a given line (row, column, or diagonal)
    def evaluate_line(line, pc_f, user_f):
        # Count how many Xs or 0s are in the line
        user_count = line.count(user_f)
        pc_count = line.count(pc_f)
        empty_count = line.count('')  # Count empty cells

        # If the line is completely filled with user's pieces, it's a strong win for the user
        if user_count == 4:
            return -1
        # If the line is completely filled with pc's pieces, it's a strong win for the pc
        if pc_count == 4:
            
            return 1
        
        elif user_count > 0 :
            if user_count == 3:  # Strong threat for user
                return -0.75
            if user_count  ==2:  # Moderate threat for user
                return -0.5
            elif user_count == 1:  # Weak threat for user
                return -0.25
        
        # If the line has some PC's pieces and no user's pieces, it's a partial sequence for the PC
        if pc_count > 0:
            if pc_count == 3:  # Strong threat for PC
                return 0.75
            elif pc_count == 2:  # Moderate threat for PC
                return 0.5
            elif pc_count == 1:  # Weak threat for PC
                return 0.25

        # If there are both user and pc pieces, it's a contested line with no immediate value
       
        return 0

    # Evaluate rows and columns
    for i in range(4):
        # Evaluate rows
        score += evaluate_line(array[i], pc_f, user_f)  # Full row
        

        # Evaluate columns
        score += evaluate_line([array[j][i] for j in range(4)], pc_f, user_f)
      
     
    # Evaluate diagonals if X or 0 is on the diagonal positions (0,0), (1,1), (2,2), (3,3)
    if array[0][0] == user_f or array[0][0] == pc_f:
       score += evaluate_line([array[i][i] for i in range(4)], pc_f, user_f)  # Main diagonal from (0,0) to (3,3)
    if array[3][0] == user_f or array[3][0] == pc_f:
        score += evaluate_line([array[i][3-i] for i in range(4)], pc_f, user_f)  # Anti-diagonal from (0,3) to (3,0)

    return score
    