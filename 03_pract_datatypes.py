# number = int(input("Enter number :: ")) # 1324
# numb_4 = number % 10 # 4
# number = number // 10 # 132
# numb_3 = number % 10 # 2
# number = number // 10 # 13
# numb_2 = number % 10 # 3
# number = number // 10 # 1
# numb_1 = number % 10 # 1
# print('{}, {}, {}, {}'.format(numb_1,numb_2,numb_3,numb_4))

# print(chr(9556) + chr(9552) * 20 + chr(9559))
# print(chr(9562) + chr(9552) * 20 + chr(9565))
# Завдання 9

# Користувач вводить з клавіатури розмір одного файлу в гігабайтах і швидкість
# інтернет-з’єднання в бітах на секунду. Порахувати, за скільки годин, хвилин і секунд
# завантажується файл.
# size = int(input("Enter size file :: "))
# speed = int(input("Enter speed downloads :: "))

# size_bit = size * 1024 * 1024 * 1024 * 8
# second = size_bit // speed

# h = second // 3600
# m = second % 3600 // 60 #(second - (h * 3600)) // 60
# second = second % 60 #second - (m * 60)
# print('{}:{}:{}'.format(h,m,second))

# Завдання 11
# Користувач вводить з клавіатури відстань, витрату бензину на 100 км і вартість трьох
# видів бензину. Вивести на екран порівняльну таблицю з вартістю подорожі на різних
# видах палива.

distance = int(input("Enter distance :: "))
volume = float(input("Enter volume :: "))

res = distance * (volume / 100)
A95 = float(input("Enter price :: "))
A92 = float(input("Enter price :: "))
A86 = float(input("Enter price :: "))

print('A95 \t :: \t {}'.format(res * A95))
print('A92 \t :: \t {}'.format(res * A92))
print('A86 \t :: \t {}'.format(res * A86))