from math import sqrt

class State:
    def __init__(self, board: list, empty: tuple, info: str):
        self.board = board
        self.empty = empty
        self.info = info

    def __str__(self):
        state = "Empty: " + str(self.empty) + " - " + self.info + "\n"
        for row in self.board:
            state += str(row) + "\n"
        return state

def clone_board(board):
    cloned = []
    for row in board:
        new_row = []
        for col in row:
            new_row.append(col)
        cloned.append(new_row)
    return cloned

def move_up(board, x, y):
    new_board = clone_board(board)
    new_board[y][x] = new_board[y-1][x]
    new_board[y-1][x] = 0
    return State(new_board, (x, y-1), "Move Up")

def move_down(board, x, y):
    new_board = clone_board(board)
    new_board[y][x] = new_board[y+1][x]
    new_board[y+1][x] = 0
    return State(new_board, (x, y+1), "Move Down")

def move_left(board, x, y):
    new_board = clone_board(board)
    new_board[y][x] = new_board[y][x-1]
    new_board[y][x-1] = 0
    return State(new_board, (x-1, y), "Move Left")

def move_right(board, x, y):
    new_board = clone_board(board)
    new_board[y][x] = new_board[y][x+1]
    new_board[y][x+1] = 0
    return State(new_board, (x+1, y), "Move Right")

def expand(state: State, N):
    x, y = state.empty
    
    descendants = []    

    cols = sqrt(N+1)-1
    
    if x == 0:
        descendants.append(move_right(state.board, x, y))
        if y == 0:
            descendants.append(move_down(state.board, x, y))
        elif y == cols:
            descendants.append(move_up(state.board, x, y))
        else:
            descendants.append(move_down(state.board, x, y))
            descendants.append(move_up(state.board, x, y))
    elif x == cols:
        descendants.append(move_left(state.board, x, y))
        if y == 0:
            descendants.append(move_down(state.board, x, y))
        elif y == cols:
            descendants.append(move_up(state.board, x, y))
        else:
            descendants.append(move_down(state.board, x, y))
            descendants.append(move_up(state.board, x, y))
    elif y == 0:
        descendants.append(move_left(state.board, x, y))
        descendants.append(move_down(state.board, x, y))
        descendants.append(move_right(state.board, x, y))
    elif y == cols:
        descendants.append(move_left(state.board, x, y))
        descendants.append(move_up(state.board, x, y))
        descendants.append(move_right(state.board, x, y))
    else:
        descendants.append(move_left(state.board, x, y))
        descendants.append(move_up(state.board, x, y))
        descendants.append(move_right(state.board, x, y))
        descendants.append(move_down(state.board, x, y))
    return descendants

def h1(board):
    h = 0
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == 0:
                continue
            if y * len(board) + x != col - 1:
                h += 1
    return h

def h2(board):
    h = 0
    goal = [[len(board) * y + x for x in range(1, len(board) + 1)] for y in range(0, len(board))]
    goal[len(board)-1][len(board)-1] = 0

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            bij = board[i][j]
            i_b = i
            j_b = j

            for i_g, r in enumerate(goal):
                for j_g, c in enumerate(r):
                    if c == bij:
                        h += (abs(i_g - i_b) + abs(j_g - j_b))

    return h