"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
MIN = -1
MAX = 1


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    nX, nO = 0, 0
    for line in board:
        for cell in line:
            if cell == X:
                nX += 1
            elif cell == O:
                nO += 1

    return O if nO < nX else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == EMPTY:
                actions.add((row, cell))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curPlayer = player(board)

    if action not in actions(board):
        raise NameError('unvalid action')

    boardCopy = copy.deepcopy(board)
    boardCopy[action[0]][action[1]] = curPlayer
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    length = len(board)

    #  row win
    for row in board:
        j = 0
        if row[j] != EMPTY:
            while j < length-1 and row[j] == row[j+1]:
                j += 1
        if (j == length-1):
            return row[j]

    # colum win
    for j in range(length):
        i = 0
        if board[i][j] != EMPTY:
            while i < length-1 and board[i][j] == board[i+1][j]:
                i += 1
        if (i == length-1):
            return board[i][j]

    for i in range(length):
        i = 0
        while i < length-1 and board[i][i] == board[i+1][i+1]:
            i += 1
        if (i == length-1):
            return board[i][i]

        i = 0
        j = length-1
        while i < length-1 and board[i][j] == board[i+1][j-1]:
            i += 1
            j -= 1
        if (i == length-1):
            return board[i][j]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    filled = True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                filled = False

    return filled or winner(board) != None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return MAX
    elif win == O:
        return MIN
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        optVal = MIN
        for action in actions(board):
            val = minValue(result(board, action), MAX)
            if val > optVal:
                optVal = val
                act = action
    else:
        optVal = MAX
        for action in actions(board):
            val = maxValue(result(board, action), MIN)
            if val < optVal:
                optVal = val
                act = action

    return act


def maxValue(board, curVal):
    if terminal(board):
        return utility(board)

    for action in actions(board):
        curVal = max(curVal, minValue(result(board, action), MAX))

    return curVal


def minValue(board, curVal):
    if terminal(board):
        return utility(board)

    for action in actions(board):
        curVal = min(curVal, maxValue(result(board, action), MIN))

    return curVal
