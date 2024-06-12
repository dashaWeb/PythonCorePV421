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

# distance = int(input("Enter distance :: "))
# volume = float(input("Enter volume :: "))

# res = distance * (volume / 100)
# A95 = float(input("Enter price :: "))
# A92 = float(input("Enter price :: "))
# A86 = float(input("Enter price :: "))

# print('A95 \t :: \t {}'.format(res * A95))
# print('A92 \t :: \t {}'.format(res * A92))
# print('A86 \t :: \t {}'.format(res * A86))


#7360 -> 2
#7360 -> 2 * 3600 / 60 -> 02
# 2:122:7360

# print(chr(9556) + chr(9552) * 10 + "Test" + chr(9552)*10 + chr(9559))
# print(chr(9562) + chr(9552) * 20 + chr(9565))

# 12:10:45  => 43845
# 15:05:05  => 54305

start_h = int(input("Enter h :: "))
start_m = int(input("Enter m :: "))
start_s = int(input("Enter s :: "))

end_h = int(input("Enter h :: "))
end_m = int(input("Enter m :: "))
end_s = int(input("Enter s :: "))

start_time = start_h * 3600 + start_m * 60 + start_s
end_time = end_h * 3600 + end_m * 60 + end_s

res_time = (end_time -start_time) // 60
print("{} uah".format(res_time * 2))