
# number = input('Enter number --> ')
# number = int(number)
# print(f'Result :: {number}')
# print('Finally')

# try:
#     number = int(input('Enter number --> '))
#     print(f'Result :: {number}')
#     print('Finally try') 
# except ValueError:
#     print('Error value')


# print('Program finally')

# try:
#     number_1 = int(input('Enter number --> '))
#     number_2 = int(input('Enter number --> '))
#     print(f'Result :: {number_1} / {number_2} = {number_1/number_2}')
#     print('Finally try') 
# except ValueError:
#     print('Error value')
# except ZeroDivisionError as ex:
#     print(f'Message :: {ex}')
# except Exception as ex:
#     print(f'Message :: {ex}')
# else:
#     print('Good')
# finally:
#     print('Finally')



# try:
#     number_1 = int(input('Enter number --> '))
#     number_2 = int(input('Enter number --> '))
#     print(f'Result :: {number_1} / {number_2} = {number_1/number_2}')
#     print('Finally try') 
# except (ValueError,ZeroDivisionError):
#     print('Error value')
# except Exception as ex:
#     print(f'Message :: {ex}')
# else:
#     print('Good')
# finally:
#     print('Finally')

# print('Program finally')

# def printNumb(numb):
#     if numb < 0:
#         raise ValueError(f'{numb} < 0')
#     if numb > 10_000:
#         raise ValueError(f'{numb} > 10 000')
#     print(f'Result :: {numb}')
# while True:  
#     numb = int(input('Enter number --> '))
#     try:
#         printNumb(numb)
#         break
#     except ValueError as msg:
#         print(f'Value Error ---- {msg}')

# print('Program finally')


# try:
#     number_1 = input('Enter number --> ')
#     age = int(input('Enter number --> '))
#     if age < 0 or age > 130:
#         raise ValueError('Text')
#     print(number_1,age)
# except (ValueError,ZeroDivisionError):
#     print('Error value')


# print('Program finally')
def printMsg(name,age):
    if age < 0 or age > 130:
        raise ValueError('Text')
    return f'Привіт, {name}! Твій вік — {age}'

# name = input('Enter name --> ')
# age = int(input("Enter age --> "))

# try:
#     print(printMsg(name,age))
# except ValueError as msg:
#     print(msg)

# def printMsg(name,age):
#     try:
#         if age < 0 or age > 130:
#             raise ValueError('Text')
#         return f'Привіт, {name}! Твій вік — {age}'
#     except ValueError:
#         print('Error value')

# printMsg('Masha',-25)

def sumList(list_):
    for numb in list_:
        if numb < 0:
            raise Exception('dfkjjdkfj')
    return sum(list_)


# numb = []
# for i in range(10):
#     numb.append(int(input('Enter --> ')))

numb = input('Enter').split(' ')
numb = [int(i) for i in numb]

try:
    print(sumList([1,2,-3,5,4,5,6]))
except Exception as text:
    print(text)

