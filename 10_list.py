
# test = [True, 'Test', 145, 45.2]
# print(test)

colors = ['red','purple','yellow','orange','blue']
print(f'Id: {id(colors)} \t Type: {type(colors)} \t Value : {colors}')
print(colors[2])

colors[2] = 'lime'
print(colors)
# colors[5] = 'pink' error
print(len(colors))
print(colors)

#[start:end:step]
print(colors[2:])
print(colors[:2])
print(colors[::2])
print(colors[::-1]) #reverse

for item in colors:
    print(item.upper())
    for chr in item:
        print(chr,' - ',end='')
    print()


print()
# Додає новий елемент в кінець списку
print(' list.append() '.center(100,'='))
print(f'\t Before :: {colors}')
colors.append('brown')
print(f'\t After  :: {colors}')

print()
# Додає новий елемент за вказаним індексом
print(' list.insert(index,value) '.center(100,'='))
print(f'\t Before :: {colors}')
colors.insert(2,'gold')
print(f'\t After  :: {colors}')


print()
# Додає список до поточного списку
print(' list.extend(list) '.center(100,'='))
print(f'\t Before :: {colors}')
colors.extend(['green','magenta','cyan'])
print(f'\t After  :: {colors}')

print()
# Видаляє останній елемент списку
print(' list.pop() '.center(100,'='))
print(f'\t Before :: {colors}')
colors.pop()
print(f'\t After  :: {colors}')

print()
# Видаляє елемент списку за індексом
print(' list.pop(2) '.center(100,'='))
print(f'\t Before :: {colors}')
colors.pop(2)
print(f'\t After  :: {colors}')


print()
# Видаляє елемент списку за вмістом
print(' list.remove(orange) '.center(100,'='))
print(f'\t Before :: {colors}')
colors.remove('orange')
print(f'\t After  :: {colors}')


print()
# Видаляє елемент списку за вмістом
print(' list.remove(orange) '.center(100,'='))
print(f'\t Before :: {colors}')
if 'orange' in colors:
    colors.remove('orange')
print(f'\t After  :: {colors}')

# colors.clear()
# print(colors)

print()
print(f'\t List :: {colors}')
ind = colors.index('green')
print(f'Index \'green\':: {ind}')


for i in range(4):
    colors.append('red')

print()
print(f'\t List :: {colors}')
ind = colors.count('red')
print(f'Index \'red\':: {ind}')

# sort [a - z]
colors.sort()
print(colors)
# sort [z - a]
colors.sort(reverse=True)
print(colors)

colors.reverse()
print(colors)

number = [1,2,5,4,7,8,5]
print(min(number))
print(max(number))
print(sum(number))
print(sorted(number))
print(sorted(number,reverse=True))


# numb = input('Enter numbers ').split(' ')
# print(numb)
# numb_str = '_'.join(numb)
# print(numb_str)
# print('_'.join(number))

# print(colors)

copy_colors = colors.copy()
print(f'Origin :: {colors}')
print(f'Clone  :: {copy_colors}')

copy_colors[0] = 'pink'

print()
print(f'Id Origin: {id(colors)}')
print(f'Id Clone : {id(copy_colors)}')
print(f'Origin :: {colors}')
print(f'Clone  :: {copy_colors}')


numb = []
for i in range(10):
    numb.append(i)
print(numb)

import random
numb = []
for i in range(10):
    numb.append(random.randint(1,20))
print(numb)

numb = [i+2 for i in range(10)]
print(numb)

numb = [random.randint(1,20) for i in range(10)]
print(numb)

numb = [i*j for i in range(1,4) for j in range(1,4)]
print(numb)

numb = []
for i in range(1,4):
    for j in range(1,4):
        numb.append(i*j)
print(numb)
numb = [str(item) for item in numb]
numb_str = '_'.join(numb)
print(numb_str)


numb =[int(i) for i in input('Enter numb :: ').split(' ')]
print(numb)