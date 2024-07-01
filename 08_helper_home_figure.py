'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

# print('*' * 1 + ' ' * 8 + '*' * 1)#line 1
# print('*' * 2 + ' ' * 6 + '*' * 2)#line 2
# print('*' * 3 + ' ' * 4 + '*' * 3)#line 3
# print('*' * 4 + ' ' * 2 + '*' * 4)#line 4
# print('*' * 5 + ' ' * 0 + '*' * 5)#line 5

# print('*' * 4 + ' ' * 2 + '*' * 4)#line 6
# print('*' * 3 + ' ' * 4 + '*' * 3)#line 7
# print('*' * 2 + ' ' * 6 + '*' * 2)#line 8
# print('*' * 1 + ' ' * 8 + '*' * 1)#line 9


# line = 5
# i = 1 # star
# j = 8 # space
# while line > 0:
#     line-=1
#     print('*' * i + ' ' * j + '*' * i)#line up
#     i+=1
#     j -= 2

# line = 4
# i = 4
# j = 2
# while line > 0:
#     line-=1
#     print('*' * i + ' ' * j + '*' * i)#line down
#     i-=1
#     j += 2

# line = int(input('Enter number of line :: '))
# if line % 2 == 0:
#     line+=1

# i = 1
# j = line - 1
# middle = line // 2
# while line > 0:
#     line-=1
#     if line >= middle:        
#         print('*' * i + ' ' * j + '*' * i)#line up
#         i+=1
#         j -= 2
#     else:
#         print('*' * i + ' ' * j + '*' * i)#line up
#         i-=1
#         j += 2
#     if line == middle:
#         i = middle
#         j = 2


'''
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
********* 
'''

# print(' ' * 0 + '*' * 9)#line 1
# print(' ' * 1 + '*' * 7)#line 1
# print(' ' * 2 + '*' * 5)#line 1
# print(' ' * 3 + '*' * 3)#line 1
# print(' ' * 4 + '*' * 1)#line 1

# print(' ' * 3 + '*' * 3)#line 1
# print(' ' * 2 + '*' * 5)#line 1
# print(' ' * 1 + '*' * 7)#line 1
# print(' ' * 0 + '*' * 9)#line 1

# line = int(input('Enter number of line :: '))
# if line % 2 == 0:
#     line+=1

# i = 0 # space 
# j = line # star 
# middle = line // 2
# while line > 0:
#     line-=1
#     if line >= middle:        
#         print(' ' * i + '*' * j)#line up
#         i+=1
#         j -= 2
#     else:
#         print(' ' * i + '*' * j)#line down
#         i-=1
#         j += 2
#     if line == middle:
#         i = middle - 1
#         j = 3