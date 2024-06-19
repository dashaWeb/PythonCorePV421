

# i = 0
# while i < 10:
#     print(f'{i} -- Hello')
#     i+=1
# else:
#     print("End")

# 1 2 3 4 5 6 7 8 9 10
# i = 0
# while i < 10:
#     i+=1
#     print(i,end='\t')


# 10 9 8 7 6 5 4 3 2 1

# i = 10
# while i >= 1:
#     print(i,end='\t')
#     i -= 1

# numb = int(input('Enter number --> '))
# i = 1
# if i < numb:
#     while i <= numb:
#         print(i,end='\t')
#         i+=1
# else:
#     while i >= numb:
#         print(i,end='\t')
#         i-=1

# i = 0
# while i < 3:
#     i+=1
#     answer = int(input('2 + 2 = ? --> '))
#     if answer == 4:
#         break
# else:
#     print('Bad')

# while True:
#     day = int(input('Enter day or 0 - exit --> '))

#     if day == 0:
#         break

#     month = int(input('Enter month --> '))
#     year = int(input('Enter year --> '))
#     if month > 12:
#         print('Error month!!!!')
#         continue

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
#         continue
    
#     if day < 10:
#         print('0', end='')
#     print(f'{day}.', end='')
#     if month < 10:
#         print('0', end='')
#     print(f'{month}.', end='')
#     print(f'{year}')


#     day += 1
#     if day > days_of_month:
#         day = 1
#         month += 1
#     if month > 12:
#         month = 1
#         year += 1

#     if day < 10:
#         print('0',end='')
#     print(f'{day}.',end='')
#     if month < 10:
#         print('0',end='')
#     print(f'{month}.',end='')
#     print(f'{year}')


# 1 x 2 = 2
# 2 x 2 = 4
# 3 x 2 = 6
# 4 x 2 = 8
# 5 x 2 = 10
# 6 x 2 = 12
# 7 x 2 = 14
# 8 x 2 = 15
# 9 x 2 = 18
# 10 x 2 = 20
# j = 1
# while j <= 10:
#     i = 0
#     while i < 10:
#         i+=1
#         print(f'{i} x {j} = {i * j}')
#     j+=1

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 5:
#         print(f'{i} x {j} = {i * j}', end='\t')
#         j+=1
#     else:
#         print()
#     i+=1
# else:
#     print()

# i = 1
# while i <= 10:
#     j = 6
#     while j <= 10:
#         print(f'{i} x {j} = {i * j}', end='\t')
#         j+=1
#     else:
#         print()
#     i+=1
# else:
#     print()

numb = 10
line = 1
start_j = 1
end = 5
while line <= 2:
    line+=1
    i = 1
    while i <= 10:
        j = start_j
        while j <= end:
            print(f'{i} x {j} = {i * j}', end='\t')
            j+=1
        else:
            print()
        i+=1
    else:
        print()
        start_j+=5
        end+=5