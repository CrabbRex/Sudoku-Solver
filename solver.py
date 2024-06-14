import pprint

N = 9


def isSafe(board, row, col, num):
    #Check row:
    for x in range(9):
        if board[row][x] == num:
            return False
    #Check column
    for x in range(9):
        if board[x][col] == num:
            return False
    #Check 3 by 3 box
    box_X = row - row % 3
    box_Y = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + box_X][j + box_Y] == num:
                return False
    return True

        
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #row, col


def solve(board, row, col):
    #base case:
    if row == N-1 and col == N :
        return True
    

    #move to next row
    if col == N:
        row += 1
        col = 0

    if board[row][col] > 0:
        return solve(board, row, col + 1)
    
    for num in range(1, 10):
        if isSafe(board, row, col, num):
            board[row][col] = num

            if solve(board, row, col + 1):
                return True
    
    #Removeing assigned num as it was wrong
        board[row][col] = 0
    return False





board = [
    [5, 7, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 2, 4, 0, 7, 8, 0],
    [4, 0, 2, 7, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [8, 2, 4, 3, 5, 1, 0, 0, 0],
    [0, 4, 7, 0, 9, 3, 1, 0, 0],
    [3, 0, 0, 4, 0, 8, 0, 5, 0],
    [0, 0, 0, 6, 0, 0, 3, 0, 0]
]

if(solve(board, 0, 0)):
    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(board)
else:
    print("No solutions")