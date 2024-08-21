
one = {
    'num':1,
    'denum':2
}

two = {
    'num':3,
    'denum':7
}

def sum_(a,b):
    denum = a['denum'] * b['denum']
    num = a['num'] * b['denum'] + b['num'] * a['denum']
    return {
        'num':num,
        'denum':denum
    }
def printRes(res):
    print(f"{res['num']} / {res['denum']}")

printRes(sum_(one,two))