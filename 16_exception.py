
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

def printNumb(numb):
    if numb < 0:
        raise ValueError(f'{numb} < 0')
    if numb > 10_000:
        raise ValueError(f'{numb} > 10 000')
    print(f'Result :: {numb}')
while True:  
    numb = int(input('Enter number --> '))
    try:
        printNumb(numb)
        break
    except ValueError as msg:
        print(f'Value Error ---- {msg}')

print('Program finally')