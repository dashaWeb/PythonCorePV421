import random
def printMessage():
    print('Hello World')


printMessage()


def sum_numb(a, b):
    return a+b

res = sum_numb(5,3)
print(res)
print(sum_numb(4,6))

lmd_message = lambda : print('Hello Lambda')
lmd_message()

sum_lmd = lambda a,b: a+b
print(sum_lmd(5,11))

def printList(list):
    for item in list:
        print(item,end='\t')
    print()

list_ = [random.randint(-20,20) for i in range(10)]
# printList(list_)

def reversItem(list):
    clone = list.copy()
    for i in range(len(list)):
        # item = item * -1
       clone[i] *= -1
    return clone

clone = reversItem(list_)
printList(list_)
printList(clone)




print(f'\n {"-"*50} \n')
print('List', end='\t\t :: ')
printList(list_)

def reverse_numb(x):
    if x < 0:
        return x
    return x * -1

def double(x):
    return x * 2

res = list(map(reverse_numb, list_))
print('List after map ', end='\t :: ')
printList(res)
res = list(map(lambda x:x*2, list_))
print('List after map ', end='\t :: ')
printList(res)


positive_numb = list(filter(lambda x : x > 0, list_))
print(f'\n {"-"*50} \n')
print('List', end='\t\t :: ')
printList(list_)
print('List after filter ', end='\t :: ')
printList(positive_numb)
even_numb = list(filter(lambda x : x % 2 == 0 and x > 0, list_))
print('List after filter ', end='\t :: ')
printList(even_numb)