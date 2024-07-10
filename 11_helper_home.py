import random

list_ = [random.randint(-10,10) for i in range(10)]

for i in list_:
    print(i,end='\t')
print()

for i in range(len(list_)):
    if list_[i] > 0:
        start_index = i
        break
for i in range(len(list_)-1,0,-1):
    if list_[i] > 0:
        end_index = i
        break
print(start_index,end_index)
sum_ = 0
for i in range(start_index+1,end_index):
    sum_ = list_[i]
print(sum_)