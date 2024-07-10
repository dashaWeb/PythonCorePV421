def printMessage(age, name=''):
    print(f'Hello {name} {age}')


printMessage(name='Masha', age=15)
printMessage(name='Oleg', age=20)
printMessage(15, 'Igor')


def sum_numb(a, b):
    # sum_ = a + b
    return a + b


def sub_numb(a, b):
    return a - b


def mult_numb(a, b):
    return a * b


def div_numb(a, b):
    if b == 0:
        print('Error!! Division by zero')
    else:
        return a / b


print(f' 2 + 3 = {sum_numb(2,3)}')
print(f' 2 - 3 = {sub_numb(2,3)}')
print(f' 2 * 3 = {mult_numb(2,3)}')
print(f' 2 / 0 = {div_numb(2,0)}')


def calculate(a, b, op):
    match op:
        case '+':
            return sum_numb(a, b)
        case '-':
            return sub_numb(a, b)
        case '*':
            return mult_numb(a, b)
        case '/':
            return div_numb(a, b)
        case _:
            print('Error!!!')


numb_1, numb_2 = 2, 5
print(f'{numb_1} + {numb_2} = {calculate(numb_1,numb_2,"+")}')
print(f'{numb_1} - {numb_2} = {calculate(numb_1,numb_2,"-")}')
print(f'{numb_1} * {numb_2} = {calculate(numb_1,numb_2,"*")}')
print(f'{numb_1} / {numb_2} = {calculate(numb_1,numb_2,"/")}')


def getOperation(line):
    if line.find('+') != -1:
        return '+'
    if line.find('-') != -1:
        return '-'
    if line.find('*') != -1:
        return '*'
    if line.find('/') != -1:
        return '/'

# reg = input('Enter ex (2 + 2) > ')
# symbol = getOperation(reg)
# numbs = [float(i) for i in reg.split(symbol)]
# print(f'{numbs[0]} {symbol} {numbs[1]} = {calculate(numbs[0],numbs[1],symbol)}')

# def sum_numb(a,b,c):
#     return a + b +c
# def sum_numb(a,b,c,d):
#     return a + b + c


def calculete_m(op, *args):
    # if op == '+':
    #     sum_ = 0
    #     for item in args:
    #         sum_+=item
    #     return sum_
    # if op == '-':
    #     sub_ = args[0]
    #     for i in range(1,len(args)):
    #         sub_-=args[i]
    #     return sub_
    # if op == '*':
    #     mult = args[0]
    #     for i in range(1,len(args)):
    #         mult*=args[i]
    #     return mult

    mult = args[0]
    for i in range(1, len(args)):
        if op == '+':
            mult += args[i]
        elif op == '-':
            mult -= args[i]
        elif op == '*':
            mult *= args[i]
        elif op == '/':
            mult /= args[i]
    return mult


print(calculete_m('+', 4, 2, 5, 8, 47, 5, 1))
print(calculete_m('-', 4, 2, 5, 8, 47, 5, 1))
print(calculete_m('*', 4, 2, 5, 8, 47, 5, 1))
print(calculete_m('/', 4, 2, 5, 8, 5, 1))
