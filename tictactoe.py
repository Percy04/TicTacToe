"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    countX = 0
    countO=0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1

    if countX > countO:
        return O
    else:
        return X




def actions(board):
    actions = set()

    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                actions.add((i,j))

    return actions 


def result(board, action):
    play = player(board)
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = play
    return new_board


def winner(board): # works
    for i in range(3): 
        if (board[i][0] == X and board[i][1] == X and board[i][2] == X):
            return X

        if (board[i][0] == O and board[i][1] == O and board[i][2] == O):
            return O
        
        if (board[0][i] == X and board[1][i] == X and board[2][i] == X):
            return X

        if (board[0][i] == O and board[1][i] == O and board[2][i] == O):
            return O

    if (board[0][0] == X and board[1][1] == X and board[2][2] == X):
        return X
    
    if (board[0][0] == O and board[1][1] == O and board[2][2] == O):
        return O

    if (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O

    if (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    countX=0
    countO=0
    if (winner(board) == None):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == X:
                    countX += 1
                elif board[i][j] == O:
                    countO += 1
    else:
        return True
    
    if (countX+countO == 9):
        return True

    return False
        


def utility(board):
    if terminal(board):
        if (winner(board) == X):
            return 1
        elif( winner(board) == O):
            return -1
        else:
            return 0

def minimax(board):
    if terminal(board):
        return None
    else:
        if (player(board) == X):
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move

def max_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    move = None
    for action in actions(board):
        temp, act = min_value(result(board, action))

        if (temp > v):
            v = temp
            move = action
            if (v == 1):
                return v, move

    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    move = None
    for action in actions(board):
        temp, act = max_value(result(board, action))

        if (temp < v):
            v = temp
            move = action
            if (v == -1):
                return v, move

    return v, move

