import random

number=[1,2,3,4,5,6,7,8,9]
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def print_board(bo):
    for i in range(9):
        if i%3==0 and i!=0:
            print("-----------------------------")
        for j in range(9):
            if j%3==0 and j!=0:
                print("| ", end="")
            if j==8:
                print(bo[i][j]," ")
            else:
                print(bo[i][j]," ", end="")


def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j]==0 or bo[i][j]=="_":
                return (i,j)
    return None


def valid(bo, num, pos):
    row=pos[0]
    col=pos[1]

    for i in range(9):    # checking the row
        if bo[row][i]==num:
            return False

    for i in range(9):  # checking the column
        if bo[i][col]==num:
            return False

    a=(row//3)*3  # // gives integer value after division
    b=(col//3)*3
    for i in range(a, a+3):  # checking the box
        for j in range(b, b+3):
            if bo[i][j]==num:
                return False
    return True


def make_board(bo):
    while True:
        copy = [row[:] for row in bo]
        cnt = 0
        while cnt < 50:
            rand = random.choice(number)
            row = random.choice(number) - 1
            col = random.choice(number) - 1
            position = (row, col)
            if valid(copy, rand, position):
                cnt += 1
                copy[row][col] = rand

        temp=[row[:] for row in copy]
        if solve(copy):
            return temp


def solve(bo):
    find=find_empty(bo)
    if not find:
        return True
    else:
        row, col=find

    for i in range(1,10):
        if valid(bo, i, find):
            bo[row][col]=i

            if solve(bo):
                return True
            else:
                bo[row][col]=0

    return False


print("Unsolved board")
print("Please wait, this may take a while.")
board=make_board(board)

solution=[row[:] for row in board]
solve(solution)

find=find_empty(board);
board[find[0]][find[1]]="_"
print_board(board)

while find_empty(board):
    missing = find_empty(board)
    r = missing[0]
    c = missing[1]
    board[r][c] = "_"

    inp = int(input("Enter the number for the blank place: "))
    print()

    if solution[r][c] == inp:
        board[r][c] = inp
        missing=find_empty(board)
        r = missing[0]
        c = missing[1]
        board[r][c] = "_"
        print_board(board)
        print("Correct Choice")
    else:
        print_board(board)
        print("Incorrect Choice, Try again.")
    print()


print("Well done, Champ!")
