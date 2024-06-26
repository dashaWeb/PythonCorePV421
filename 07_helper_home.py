# Користувач вводить будь-яке ціле число. Необхідно з цього цілого числа видалити всі цифри 3 і 6 і вивести назад на екран.

# numb = input('Enter number -> ')

# result = ''
# # 12458786
# for i in numb:
#     if i != '3' and i != '6':
#         result += i
# print(int(result))

numb = int(input('Enter number -> '))

result = 0
mult = 1

while numb != 0:
    digit = numb % 10
    numb //= 10
    if digit == 3 or digit == 6:
        continue
    result += digit * mult
    mult *=10

print(result)