# word = 'Hello'
# for letter in word:
#     print(letter + ' _ ', end='')

# for i in range(10):
#     print(i+1, end='\t')

# for i in range(1, 10 + 1):
#     print(i, end='\t')


# numb = int(input('Enter number : '))
# for i in range(1,numb + 1,2):
#     print(i, end='\t')
# else:
#     print()


# numb = int(input('Enter number :: ')) #8
# counter = 0
# # range() --> 1 2 3 4 5 6 7 8
# # 8 % 1 -> true
# # 8 % 2 -> true
# # 8 % 3 -> false
# # 8 % 4 -> true
# # 8 % 5 -> false
# # 8 % 6 -> false
# # 8 % 7 -> false
# # 8 % 8 -> true
# for i in range(1, numb+1):
#     if numb % i == 0:
#         counter+=1

# if counter > 2:
#     print('Complex number')
# else:
#     print('Prime number')


# numb = int(input('Enter number :: '))  # 8
# flag = True

# for i in range(2, numb//2+1):
#     if numb % i == 0:
#         flag = False
#         break
# if not flag:
#     print('Complex number')
# else:
#     print('Prime number')



# for i in range(5):
#     # rnd = random.random() # 0 - 1
#     # rnd = int(random.random() * 10) + 1 # 0 - 1
#     # rnd = random.randint(1,10)
#     rnd = random.choice('srp')
#     print(rnd)
#     input()

import random
while True:
    user_score = 0
    bot_score = 0
    for i in range(3):

        while True:
            print('-'*15 + f' Round #{i+1} ' + '-'*15)
            user = input('''
            [r] - rock
            [p] = paper
            [s] = scissors
                Enter your choose :: ''')
            if user == 'r' or user == 'p' or user == 's':
                break
            else:
                print('Error! Enter true choose')
        bot = random.choice('srp')

        print(f'\t\t Bot \t User')
        print(f'\t\t [{bot}] \t [{user}]')
        if user == 'p' and bot == 'r' or user == 'r' and bot == 's' or user == 's' and bot == 'p':
            user_score += 1
        elif bot == 'p' and user == 'r' or bot == 'r' and user == 's' or bot == 's' and user == 'p':
            bot_score += 1

    if user_score > bot_score:
        print('='*15 + ' Congratulation!!! ' + '='*15)
    elif bot_score > user_score:
        print('='*15 + ' Sorry!!! You Loser( ' + '='*15)
    else:
        print('='*15 + ' Draw ' + '='*15)

    exit = input('Play again? [n] - no; [y] - yes -->')
    if exit == 'n':
        break

# 1 - Реалізувати можливість (розпочати гру знову)
# 2 - Розширити гру додавши нові варіант (ящірка, спок)
# 3 - Збільшити кількість раундів до 5-ти
# Коли користувач завершить гру (вийшов) - показати статистику по всій грі
#  User won - 2
#  Bot  won - 2
#  Draw - 2

