# ==, <, >, <=, >=, !=

# a = 5
# b = 7
# password = 'mka5'

# d = c = 9

# print(f'{password} == mka5  --> {password == "mka5"}')  # True
# print(f'{a} == {b}  --> {a == b}')  # False
# print(f'{a} < {b}  --> {a < b}')  # True
# print(f'{a} > {b}  --> {a > b}')  # False
# print(f'{d} > {c}  --> {d > c}')  # False
# print(f'{d} >= {c}  --> {d >= c}')  # True
# print(f'{d} <= {c}  --> {d <= c}')  # True
# print(f'{d} != {c}  --> {d != c}')  # False


# and
# or
# login = 'dev'
# password = 'mka5'
# print(login == 'mka' and password == 'mka5')

# month = int(input("Enter number month :: "))
# print(month == 1 or month == 3 or month == 5 or month == 7)

# print('Apple' + 2) # Error
# print(5 + True)

# year = int(input("Enter year :: "))
# days = 365 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# print(f'In {year} year = {days} days')

# age = int(input("Enter age :: "))
# if age >= 18:
#     print("Hello")
# else: 
#     print("Error")


# day = int(input('Enter number day :: '))
# if day == 1:
#     print('Monday')
# elif day == 2:
#     print('Tuesday')
# elif day == 3:
#     print('Wednesday')
# else:
#     print('Error')



login = input('Хто прийшов? ')
if login == 'Адмін':
    password = input('Пароль? ')
    if password == 'ШАГ':
        print('Ласкаво просимо !!! ')
    elif password.lower() == 'Скасувати'.lower():
        print('Вхід скасований')
    else:
        print('Пароль невірний')
elif login.lower() == 'Скасувати'.lower():
    print('Вхід скасований')
else:
    print('Я вас не знаю !!!')


chs = input('''
    1 - Sum
    2 - Sub
    3 - Avg
    4 - Mult
    Enter :: ''')
if chs == '1':
    print( 2 + 3)
else:
    print('Error')
