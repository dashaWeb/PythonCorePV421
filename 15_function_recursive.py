
'''
    5! = 5 * 4!
    4! = 4 * 3!
    3! = 3 * 2!
    2! = 2 * 1!
    1! = 1 * 0!
    0! = 1
'''


def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


print(factorial(5))


'''
    sum(1-5) -> 1 + sum(2-5)
    sum(2-5) -> 2 + sum(3-5)
    sum(3-5) -> 3 + sum(4-5)
    sum(4-5) -> 4 + sum(5-5)
    sum(5-5) -> 5
'''


def sumRange(start, end):
    if start == end:
        return start
    return start + sumRange(start+1, end)


print(sumRange(1, 5))

'''
    2^4 --> 2 * 2^3
    2^3 --> 2 * 2^2
    2^2 --> 2 * 2^1
    2^1 --> 2
'''


def powRec(numb, pow):
    if pow == 1:
        return numb
    return numb * powRec(numb, pow-1)


print(powRec(2, 4))


# n = 6
def star(n):
    if n > 0:
        print('*', end='')
        star(n - 1)


star(6)

def pal(numb):
    line = str(numb)
    if numb < 10:
        return str(numb)
    return line[-1] + pal(numb // 10)


print(pal(123456))


def pr(n):
    if n > 0:
        print('(',end='')
        pr(n-1)
        print(')',end='')
pr(5)

