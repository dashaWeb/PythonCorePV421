

print(3, type(3)) # number (int)
print(3.5, type(3.5)) # number (float)
print('3.5', type('3.5')) # string (str)
print(True, type(True)) # boolean (bool)
#None

first_name = "Masha"
first_Name = "Pasha"
age = 18
PI = 3.14
flag = True

print(first_name,first_Name,age,PI,flag)

#print(first_name + first_Name + age + PI + flag)#TypeError: can only concatenate str (not "int") to str
#16.11.09 (14 років)
day = 16
month = 11
year = 2009
age = 14
# print(day,month,year,age,'років',sep='.')
print('{}.{}.{} ({} років)'.format(day,month,year,age))

# **, //, %
# *,/
# -,+

numb_1 = 2
numb_2 = 3
# 2 + 3 = 5
res_sum = numb_1 + numb_2
print('{} + {} = {}'.format(numb_1,numb_2,res_sum))

# 2 - 3 = 5
res_sub = numb_1 - numb_2
print('{} - {} = {}'.format(numb_1,numb_2,res_sub))

# 2 * 3 = 5
res_mult = numb_1 * numb_2
print('{} * {} = {}'.format(numb_1,numb_2,res_mult))

# 2 / 3 = 5
res_div = numb_1 / numb_2
print('{} / {} = {}'.format(numb_1,numb_2,res_div))

# 2 ** 3 = 5
res_div = numb_1 ** numb_2
print('{} ** {} = {}'.format(numb_1,numb_2,res_div))

# 2 // 3 = 5
res_div = numb_1 // numb_2
print('{} // {} = {}'.format(numb_1,numb_2,res_div))

# 2 % 3 = 5
res_div = numb_1 % numb_2
print('{} % {} = {}'.format(numb_1,numb_2,res_div))

one = 3.5 #float
two = 5 # int

res = one + two

res = two + True
#  True = 1, False = 0
print(type(res), res)

# int()
# float()
# str()

number = 7.9
print(int(number)) #7

line = "number : " + str(number)
print(line)

# one = float(input("Enter first number : "))
# two = input("Enter second number : ")
# two = float(two)

# print("Sum :: {}".format(one + two))

# print('lorem' * 40)

# one = 5
# two = 7

# one,two = 5,7

# one = 3
# two = 3
# one = two = 3

# age = age + 1
# age += 1
# +=, -=, *=, /=, **=, //=, %=

# number = 45
# # 45 / 10 = int(4.5) => 4
# one = number // 10
# two = number % 10
# print(one,two,sep='\n')


summ = 1500 
percent = 20

#1
# sale = summ / 100 # => 1% = 15
# sale = sale * percent
sale = summ / 100 * percent

#  100% = 1
#  20%  = 0.2
# 20 / 100
print(summ * (percent / 100))

# 25 / 10 => 2.5
# 25 // 10 => 2


####### helper
# Завдання 1
# Користувач вводить із клавіатури два числа. Необхідно знайти суму чисел, різницю
# чисел, добуток чисел. Результат обчислень вивести на екран.

# one = float(input("Enter number :: "))
# two = float(input("Enter number :: "))

# res_sum = one + two
# print('{} + {} = {}'.format(one,two,res_sum))

# # 2 - 3 = 5
# res_sub = one - two
# print('{} - {} = {}'.format(one,two,res_sub))

# # 2 * 3 = 5
# res_mult = one * two
# print('{} * {} = {}'.format(one,two,res_mult))

# # Завдання 2

# # Користувач вводить із клавіатури два числа. Перше число — це значення, друге чи-
# # сло — відсоток, який необхідно вирахувати. Наприклад, ми ввели з клавіатури 50 і
# # 10. Потрібно вивести на екран 10 відсотків від 50. Результат
# # 5.

# one = int(input("Enter number :: "))
# two = int(input("Enter number :: "))
# print('Result :: {}'.format(one / 100 * two))

# # Завдання 3
# # Напишіть програму, що обчислює площу прямокутника. Користувач із клавіатури
# # вводить ширину і висоту прямокутника.
# width = int(input("Enter width :: "))
# height = int(input("Enter height :: "))
# print('Result :: {}'.format(one * two))



# numb = 12458
# e = numb % 10 # => 12458 % 10 = 8
# numb //= 10 # numb(12458) // 10 => 1245   delete.8 
# d = numb % 10 # => 1245 % 10 = 5
# numb //= 10 # numb(1245) // 10 => 124   delete.5 
# a = numb % 10 # => 124 % 10 = 4
# numb //= 10 # numb(124 // 10 => 12   delete.4
# b = numb % 10 # 2
# c = numb // 10 # 1

# e *= 10000 # 80000

num = 8234#int(input("Введіть ЧОТИРЬОХзначне число"))
num1 = (num // 1000)
print(num, num1)
num2 = (num // 100 % 10)
print(num, num2)
# 8234 // 10 => 823 %10
num3 = (num // 10 % 10)
print(num, num3)
num4 = (num % 10) 
print(num, num4)
Dob = num1 * num2 * num3 * num4
print (Dob)
