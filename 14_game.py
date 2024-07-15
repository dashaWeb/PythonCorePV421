
board = ['X' for i in range(9)]


def printBoard(board):
    for i in range(1,len(board)+1):
        print(f' {board[i-1]} ', end='')
        if i % 3 != 0:
            print(chr(9553),end='')
        if i % 3 == 0:
            print()
            if i == len(board):
                break
            for j in range(3):
                print(chr(9552)*3,end='')
                if j == 2:
                    break
                print(chr(9580),end='')
            print()
printBoard(board)