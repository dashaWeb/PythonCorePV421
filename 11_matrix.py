import random
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix)


row, col = 3,3

# matrix = []
# # for i in range(row):
# #     row_matrix = []
# #     for j in range(col):
# #         row_matrix.append(random.randint(1,20))
# #     matrix.append(row_matrix)

# # row_1 = [random.randint(1,20) for i in range(col)] # [0,1,2,3,4]
# # row_2 = [random.randint(1,20) for i in range(col)] # [0,1,2,3,4]
# # row_3 = [random.randint(1,20) for i in range(col)] # [0,1,2,3,4]

# for i in range(row):
#     matrix.append([random.randint(1,20) for i in range(col)])

matrix = [[random.randint(1,20) for i in range(col)] for j in range(row)]
for row in matrix:
    for numb in row:
        print(numb, end='\t')
    print()


# for j in range(len(matrix)):
#     for i in range(len(matrix[j])):
#         print(matrix[j][i], end='\t')
#     print()
# sum_ = 0
# for row in matrix:
#     for numb in row:
#         sum_+= numb
# print(f'Sum :: {sum_}')
# sum_ = 0
# for row in matrix:
#     sum_ += sum(row)

sum_ = sum([sum(row) for row in matrix])
print(f'Sum :: {sum_}')

# max_ = matrix[0][0]
# min_ = matrix[0][0]
# for row in matrix:
#     for item in row:
#         if max_ < item:
#             max_ = item
#         if min_ > item:
#             min_ = item

max_ = max([max(row) for row in matrix])
min_ = min([min(row) for row in matrix])

print(f'Max :: {max_}')
print(f'Min :: {min_}')