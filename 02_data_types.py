

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