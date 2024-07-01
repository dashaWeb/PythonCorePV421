
# month = int(input('Enter month --> '))
# offset = int(input('Enter start number day --> '))

# if month == 3 or month == 5 or month == 7 or month == 1 or month == 8 or month == 10 or month == 12:
#     days_of_month = 31
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     days_of_month = 30
# elif month == 2:
#     year = int(input('Enter Year --> '))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         days_of_month = 29
#     else:
#         days_of_month = 28
# offset -= 1
# counter = 0
# line = (days_of_month + offset) // 7
# print('  \t' * offset, end='')
# for i in range(1,days_of_month + 1):
#     if i < 10:
#         print(f'0{i}\t',end='')
#     else:
#         print(f'{i}\t',end='')
#     if (i + offset) % 7 == 0:
#         print()
#         counter+=1
#         line-=1
#         if i - 1 > 0:
#             counter+=1
#     if line == 0 and (days_of_month + offset) % 7 == 6 and i == days_of_month:
#         counter+=1
# print()
# print(counter) 

# 2. Створити програму, яка виводить на екран прості числа в
# діапазоні від 2 до 1000. (Число називається простим, якщо воно
# ділиться тільки на 1 і на саме себе без залишку; причому числа 1
# і 2 за прості не вважаються).

# for numb in range(2,1001):
#     flag = True
#     for i in range(2, numb//2+1):
#         if numb % i == 0:
#             flag = False
#             break
#     if flag:
#         print(numb)

counter = 0
for i in range(100,1000):
    numb = i
    a = numb % 10
    numb//=10
    b = numb%10
    c= numb//10
    if a != b and b != c:
        print(i)
        counter+=1
