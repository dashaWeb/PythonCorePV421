
# day = input('Enter number of day --> ')
# match int(day): # day == 1
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case _:
#         print('Error')


# month = int(input('Enter month --> '))
# match month:
#     case 1:
#         days = 31
#     case 3:
#         days = 31
#     case 5:
#         days = 31
#     case 7:
#         days = 31
#     case 8:
#         days = 31
#     case 10:
#         days = 31
#     case 12:
#         days = 31
#     case 4:
#         days = 30
#     case 6:
#         days = 30
#     case 9:
#         days = 30
#     case 11:
#         days = 30
#     case 2:
#         year = int(input('Enter year --> '))
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             days = 29
#         else:
#             days = 28
#     case _:
#         print('Error')
#         days = None
    # 04.05.2004 --> 05.05.2004
    # 31.03.2004 --> 01.04.2004
    # 31.12.2005 --> 01.01.2005
    # 30.04.2004 --> 01.05.2004
    # 28.02.2004 --> 29.02.2004
# day = int(input('Enter day --> '))
# month = int(input('Enter month --> '))
# year = int(input('Enter year --> '))

# if day < 10:
#     print('0',end='')
# print(f'{day}.',end='')
# if month < 10:
#     print('0',end='')
# print(f'{month}.',end='')
# print(f'{year}')
# if month > 12:
#     print('Error month!!!!')
# else:
#     if month == 3 or month == 5 or month == 7 or month == 1 or month == 8 or month == 10 or month == 12:
#         days_of_month = 31
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         days_of_month = 30
#     elif month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             days_of_month = 29
#         else:
#             days_of_month = 28

#     if day > days_of_month:
#         print('Error day !!!!')
#     else:
#         day += 1
#         if day > days_of_month:
#             day = 1
#             month += 1
#         if month > 12:
#             month = 1
#             year += 1

#         if day < 10:
#             print('0',end='')
#         print(f'{day}.',end='')
#         if month < 10:
#             print('0',end='')
#         print(f'{month}.',end='')
#         print(f'{year}')

# import datetime
from datetime import date

one = date(2024,6,17)
two = date(2024,6,14)
print((one - two).days)
