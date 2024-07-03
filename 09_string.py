
word = 'Length'

# print(word[2])
# word[2] = 'N' error
# for i in range(0,256):
#     print(chr(i), i, end='\t')
#     if i % 15 == 0:
#         print()

# letter = 'w'
# print(letter)
# print(ord(letter))
# lower_lett = chr(ord(letter) - 32)
# print(lower_lett)


# line = '{0} Login :: {1} \n {1} Password :: {0}'.format('Admin',"123456qwerty")
# print(line)
# line = r'\n - Enter; \t - Tab'
# print(line)


# line = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
# print(line[2]) # r
# length = len(line)
# print(f'Length :: {length}')
# print(line[length-1])
# print(line[-1])

# # [start:end:step]
# # print(line[-1:6:-2])
# print(line[6:])
# print(line[:20])
# print(line[::2])
# print(line[::-1])





# import re

# numbers = '12345874'
# letters = 'jghujdmffbvg'
# line = 'Lorem ipsum emet dolor'
# word = 'Fruit Apple'
# word_2 = "BANANA"
# letterDig = 'hfgt3546jfhfy'

# # лише букви або цифри
# print('\n\n================== isalnum() =================')
# print('\t', numbers, '\t--- >\t', numbers.isalnum())
# print('\t', letters, '\t--- >\t', letters.isalnum())
# print(line, ' --- >\t', line.isalnum())
# print('\t', word, '\t--- >\t', word.isalnum())
# print('\t', word_2, '\t--- >\t', word_2.isalnum())
# print('\t', letterDig, '\t--- >\t', letterDig.isalnum())
# print('==================================================')

# print('\n\n================== isalpha() =================')  # лише букви
# print('\t', numbers, '\t--- >\t', numbers.isalpha())
# print('\t', letters, '\t--- >\t', letters.isalpha())
# print(line, ' --- >\t', line.isalpha())
# print('\t', word, '\t--- >\t', word.isalpha())
# print('\t', word_2, '\t--- >\t', word_2.isalpha())
# print('\t', letterDig, '\t--- >\t', letterDig.isalpha())
# print('==================================================')

# print('\n\n================== isdigit() =================')  # лише цифри
# print('\t', numbers, '\t--- >\t', numbers.isdigit())
# print('\t', letters, '\t--- >\t', letters.isdigit())
# print(line, ' --- >\t', line.isdigit())
# print('\t', word, '\t--- >\t', word.isdigit())
# print('\t', word_2, '\t--- >\t', word_2.isdigit())
# print('\t', letterDig, '\t--- >\t', letterDig.isdigit())
# print('==================================================')

# # letters = '           '
# print('\n\n================== isspace() =================')  # лише пропуск
# print('\t', numbers, '\t--- >\t', numbers.isspace())
# print('\t', letters, '\t--- >\t', letters.isspace())
# print(line, ' --- >\t', line.isspace())
# print('\t', word, '\t--- >\t', word.isspace())
# print('\t', word_2, '\t--- >\t', word_2.isspace())
# print('\t', letterDig, '\t--- >\t', letterDig.isspace())
# print('==================================================')


# # перевірка букви на нижній регістр
# print('\n\n================== islower() =================')
# print('\t', numbers, '\t--- >\t', numbers.islower())
# print('\t', letters, '\t--- >\t', letters.islower())
# print(line, ' --- >\t', line.islower())
# print('\t', word, '\t--- >\t', word.islower())
# print('\t', word_2, '\t--- >\t', word_2.islower())
# print('\t', letterDig, '\t--- >\t', letterDig.islower())
# print('==================================================')


# # перевірка букви на верхній регістр
# print('\n\n================== isupper() =================')
# print('\t', numbers, '\t--- >\t', numbers.isupper())
# print('\t', letters, '\t--- >\t', letters.isupper())
# print(line, ' --- >\t', line.isupper())
# print('\t', word, '\t--- >\t', word.isupper())
# print('\t', word_2, '\t--- >\t', word_2.isupper())
# print('\t', letterDig, '\t--- >\t', letterDig.isupper())
# print('==================================================')


# #  першої букви у слові на верхній регістр
# print('\n\n================== istitle() =================')
# print('\t', numbers, '\t--- >\t', numbers.istitle())
# print('\t', letters, '\t--- >\t', letters.istitle())
# print(line, ' --- >\t', line.istitle())
# print('\t', word, '\t--- >\t', word.istitle())
# print('\t', word_2, '\t--- >\t', word_2.istitle())
# print('\t', letterDig, '\t--- >\t', letterDig.istitle())
# print('==================================================')


# print('\n\n================== lower() =================')
# print('\t', numbers, '\t--- >\t', numbers.lower())
# print('\t', letters, '\t--- >\t', letters.lower())
# print(line, ' --- >\t', line.lower())
# print('\t', word, '\t--- >\t', word.lower())
# print('\t', word_2, '\t--- >\t', word_2.lower())
# print('\t', letterDig, '\t--- >\t', letterDig.lower())
# print('==================================================')


# print('\n\n================== upper() =================')
# print('\t', numbers, '\t--- >\t', numbers.upper())
# print('\t', letters, '\t--- >\t', letters.upper())
# print(line, ' --- >\t', line.upper())
# print('\t', word, '\t--- >\t', word.upper())
# print('\t', word_2, '\t--- >\t', word_2.upper())
# print('\t', letterDig, '\t--- >\t', letterDig.upper())
# print('==================================================')


# print('\n\n================== capitalize() =================')
# print('\t', numbers, '\t--- >\t', numbers.capitalize())
# print('\t', letters, '\t--- >\t', letters.capitalize())
# print(line, ' --- >\t', line.capitalize())
# print('\t', word, '\t--- >\t', word.capitalize())
# print('\t', word_2, '\t--- >\t', word_2.capitalize())
# print('\t', letterDig, '\t--- >\t', letterDig.capitalize())
# print('==================================================')


# print('\n\n================== title() =================')
# print('\t', numbers, '\t--- >\t', numbers.title())
# print('\t', letters, '\t--- >\t', letters.title())
# print(line, ' --- >\t', line.title())
# print('\t', word, '\t--- >\t', word.title())
# print('\t', word_2, '\t--- >\t', word_2.title())
# print('\t', letterDig, '\t--- >\t', letterDig.title())
# print('==================================================')


# print('\n\n================== swapcase() =================')
# print('\t', numbers, '\t--- >\t', numbers.swapcase())
# print('\t', letters, '\t--- >\t', letters.swapcase())
# print(line, ' --- >\t', line.swapcase())
# print('\t', word, '\t--- >\t', word.swapcase())
# print('\t', word_2, '\t--- >\t', word_2.swapcase())
# print('\t', letterDig, '\t--- >\t', letterDig.swapcase())
# print('==================================================')

# line += ' ipsum lorem dolor ipsum'

# print('\n\n================== find(substr,startindex=default,endindex=default) =================\n')

# print('\t ', line, ' --- >\t', line.find('ipsum'))
# print('\t ', line, ' --- >\t', line.find('ipsum', 7))
# print('\t ', line, ' --- >\t', line.find('ipsum', 24))
# print('\t ', line, ' --- >\t', line.find('ipsum', 42))

# print('\n\n================== find() =================\n')
# index = -1
# while True:
#     index = line.find('ipsum', index+1)
#     if index == -1:
#         break
#     print('\t ', line, ' --- >\t', index)

# print('\n==================================================')

# print('\n\n================== find() =================\n')
# index = -1
# while True:
#     index = line.lower().find('lorem', index+1)
#     if index == -1:
#         break
#     print('\t ', line, ' --- >\t', index)

# print('\n==================================================')


# print('\n\n================== rfind(substr,startindex=default,endindex=default) =================\n')

# print('\t ', line, ' --- >\t', line.rfind('ipsum'))

# print('\n\n================== find() =================\n')


# print('\n\n================== index() =================\n')

# print('\t ', line, ' --- >\t', line.index('ipsum'))
# print('\t ', line, ' --- >\t', line.index('ipsum', 7))
# print('\t ', line, ' --- >\t', line.index('ipsum', 24))
# # print('\t ', line, ' --- >\t', line.index('ipsum', 42))

# print('\n\n============================================\n')

# print('\n\n================== rindex() =================\n')

# print('\t ', line, ' --- >\t', line.rindex('ipsum'))
# print('\t ', line, ' --- >\t', line.rindex('ipsum', 0, 40))
# print('\t ', line, ' --- >\t', line.rindex('ipsum', 0, 22))
# # print('\t ', line, ' --- >\t', line.rindex('ipsum', 0, 5))

# print('\n\n============================================\n')


# print('\n\n================== count() =================\n')
# print('\t ', line, ' --- >\t', line.count('ipsum'))
# print('\n\n============================================\n')


# print('\n\n================== replace() =================\n')
# print('\t ', line, ' --- >\t', line.replace('ipsum', 'yellow'))
# print('\n\n============================================\n')


# str_1 = '123'
# str_2 = '234'
# str_3 = 'Lorem** 21 ipsum red'


# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_1, '\t\t\t --- >\t', re.search('12', str_1))
# print('\t ', str_2, '\t\t\t --- >\t', re.search('12', str_2))
# print('\t ', str_3, '\t --- > \t', re.search('12', str_3))
# print('\n\n============================================\n')

# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_1, '\t\t\t --- >\t', re.search('[12]', str_1))
# print('\t ', str_2, '\t\t\t --- >\t', re.search('[12]', str_2))
# print('\t ', str_3, '\t --- > \t', re.search('[12]', str_3))
# print('\n\n============================================\n')


# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_1, '\t\t\t --- >\t', re.search('[0-9]', str_1))
# print('\t ', str_2, '\t\t\t --- >\t', re.search('[0-9]', str_2))
# print('\t ', str_3, '\t --- > \t', re.search('[0-9]', str_3))
# print('\n\n============================================\n')


# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_1, '\t\t\t --- >\t', re.search('[a-z]', str_1))
# print('\t ', str_2, '\t\t\t --- >\t', re.search('[a-z]', str_2))
# print('\t ', str_3, '\t --- > \t', re.search('[a-z]', str_3))
# print('\n\n============================================\n')

# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_1, '\t\t\t --- >\t', re.search('[a-z]', str_1))

# match = re.search('[a-z]', str_1)
# if match:
#     print("Find by letter")
# else:
#     print('not found letter')

# match = re.search('[a-zA-Z]', str_3)
# print('\t ', str_3, '\t\t\t --- >\t', re.search('[a-zA-Z]', str_3))

# if match:
#     print("Find by letter")
# else:
#     print('not found letter')
# print('\n\n============================================\n')

# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_1, '\t\t\t --- >\t', re.search('[a-zA-Z]{5}', str_1))
# print('\t ', str_2, '\t\t\t --- >\t', re.search('[a-zA-Z]{5}', str_2))
# print('\t ', str_3, '\t --- > \t', re.search(' [a-zA-Z]{5}', str_3))
# print('\n\n============================================\n')


# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_1, '\t\t\t --- >\t', re.search('[a-zA-Z]{3}\W', str_1))
# print('\t ', str_2, '\t\t\t --- >\t', re.search('[a-zA-Z]{3}\W', str_2))
# print('\t ', str_3, '\t --- > \t', re.search(' [a-zA-Z]{3}$', str_3))
# print('\n\n============================================\n')


# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_3, '\t --- > \t', re.search('^\w+', str_3))
# print('\n\n============================================\n')


# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_3, '\t --- > \t', re.search('[^Lorem]', str_3))
# print('\n\n============================================\n')


# print('\n\n================== re.search("template",str)  =================\n')
# print('\t ', str_3, '\t --- > \t', re.search('Lorem\**', str_3).group(0))
# print('\n\n============================================\n')

# print('\n\n================== re.search("template",str)  =================\n')
# match = re.findall('\w+', str_3)
# print('\t ', str_3, '\t --- > \t', re.findall('\w+', str_3))
# print('\n\n============================================\n')
# for item in match:
#     print(item)

# print('\t ', str_3, '\t --- > \t', re.sub('\w{3}$', 'yellow', str_3))
# print(str_3[-1::-1])

# line = 'Th4ere2 5 6 8 a4re'
# # print(line[0:len(line):2])
# #0 1 2 3 4 5 6 7 8 
# #
# # for i in range(len(line)):
# #     print(line[len(line)-1-i],end="") 

# # print(line[::-1])
# dig = 0
# let = 0
# for item in line:
#     if item.isalpha():
#         let+=1
#         continue
#     if item.isdigit():
#         dig+=1
# print('Letters :: ',let)    
# print('Digits :: ',dig)    

# print(line.count('r'))


# print(line.replace('r','qqqqq'))
# line = 'apple orange banana plum'
# print(line.split(' ')[0])




import string
import random
print('Lorem'.center(50))
print('Lorem'.center(50,'*'))
print('\tLorem\t  rr'.expandtabs(10))
print('Lorem'.rjust(30,'*'))
print('Lorem'.ljust(30,'='))
print('Lomrem'.lstrip('Lo'))
print('Lomrem'.rstrip('m'))
print('mLomrmem'.strip('m'))
print('L124'.zfill(10))

print("ttest {0:3.2f}".format(2.36589))
print("ttest {0:4d}".format(20))
print("ttest {0:^10}".format(20))
print("ttest {0:>10}".format(20))
print("ttest {0:<10}!!!".format(20))

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

userLogin = ''.join(random.sample((string.ascii_lowercase),6))
userPass = ''.join(random.sample((string.ascii_letters+string.digits+string.punctuation),8))
print(userLogin)
print(userPass)