"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_moves_X = 0
    count_moves_O = 0
    
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == X:
                count_moves_X += 1
            elif board[row][column] == O:
                count_moves_O += 1
    
    if count_moves_X == count_moves_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    every_possible_actions = set()
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == EMPTY:
                every_possible_actions.add((row, column))
    return every_possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if action not in actions(board):
        raise Exception(IndexError)
    
    b_copy = copy.deepcopy(board)
    b_copy[i][j] = player(b_copy)
    return b_copy


def check_rows(board, player):
    for row in range(len(board)):
        count = 0
        for column in range(len(board[0])):
            if board[row][column] == player:
                count += 1
        if count == len(board[0]):
            return True
    return False


def check_columns(board, player):
    for column in range(len(board[0])):
        count = 0
        for row in range(len(board)):
            if board[row][column] == player:
                count += 1
        if count == len(board):
            return True
    return False


def check_up_down(board, player):
    count = 0
    for row in range(len(board)):
        if board[row][row] == player:
            count += 1
    return count == len(board)



    
def tie(board):
    count_Empty = (len(board) * len(board[0]))
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] is not EMPTY:
                count_Empty -= 1
    return count_Empty == 0

def is_tie(board):
    count_empty = (len(board) * len(board[0]))
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] is not EMPTY:
                count_empty -= 1
    return count_empty == 0

    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or is_tie(board):
        return True
    else:
        return False
    
    
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    
def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    #Case of player is X (max-player)
    elif player(board) == X:
        moves = []
        # Loop over possible actions
        for action in actions(board):
            moves.append([min_value(result(board, action)),action])
        return sorted(moves, key = lambda x: x[0], reverse = True)[0][1]
    
    #Case of player is O
    elif player(board) == O:
        moves = []
        # Loop over possible actions
        for action in actions(board):
            moves.append([max_value(result(board, action)),action])
        return sorted(moves, key = lambda x: x[0])[0][1]
    
    
    