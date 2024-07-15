import random

board = [' ' for i in range(9)]

def check(board,a,b,c):
    return board[a] == board[b] and board[a] == board[c]

def checkWin(board):
    if board[0] != ' ':
        if check(board,0,1,2) or check(board,0,3,6) or check(board,0,4,8):
            return board[0]
    if board[1] != ' ':
        if check(board,1,4,7):
            return board[1]
    if board[2] != ' ':
        if check(board,2,4,6) or check(board,2,5,8):
            return board[2]
    if board[3] != ' ':
        if check(board,3,4,5):
            return board[3]
    if board[6] != ' ':
        if check(board,6,7,8):
            return board[6]

def printBoard(board):
    counter = 0
    for i in range(1,len(board)+1):
        print(f' {board[i-1]} ', end='')
        if i % 3 != 0:
            print(chr(9553),end='')
        if i % 3 == 0:
            print('\t\t',end='')
            for j in range(3):
                counter+=1
                print(f' {counter} ', end='')
                if j == 2:
                    break
                print(chr(9553),end='')
            print()
            if i == len(board):
                break
            for j in range(2):
                for j in range(3):
                    print(chr(9552)*3,end='')
                    if j == 2:
                        break
                    print(chr(9580),end='')
                print('\t\t',end='')
            print()
printBoard(board)

user = 'X'
bot = 'O'
flag = True
count = 9

# [1 - 9]
while count > 0:
    if flag:
        step = int(input('Enter cell number > ')) - 1
        if board[step] != ' ':
            continue
        board[step] = user
        flag = False
        count-=1
    else:
        cell = random.randint(0,8)
        if board[cell] != ' ':
            continue
        board[cell] = bot
        flag = True
        count-=1
    print()
    printBoard(board)
    win = checkWin(board)
    if win != None:
        break
if win == user:
    print(f"Win User {user}")
elif win == bot:
    print(f"Win bot {bot}")
else:
    print('Draw')





# 1. Доробити гру X vs 0; (Почали робити на парі);
# 2. Додати функціонал повторення гри (Після того, як показали результат гри, запитати у користувача, чи бажає він повторити гру. Якщо користувач обирає варіант "так" - гра починається з початку,"ні" - оформити завершення  гри ).
# 3. Налаштувати початок гри (щоб чергувалось X або O). 
# 4*. додати інтелект для комп'ютера.
# 	Мається на увазі, щоб комп'ютер перевіряв де вже стоять хрестики. Якщо користувачу залишається поставити один хрести для перемоги, комп'ютер повинен поставити туди 0, тим самим не дати виграти користувачу.