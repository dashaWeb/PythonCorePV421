import random

row, col = 3, 4

matrix = [[random.randint(1,60) for i in range(col)] for j in range(row)]
matrix2 = [random.randint(1,60) for i in range(4)]

all_matrix = [matrix, [matrix2]]

for i in range(len(all_matrix)):
    for j in range(len(all_matrix[i])):
        for k in range(len(all_matrix[i][j])):
            print(all_matrix[i][j][k], end='\t')
        print(f"|\t{sum(all_matrix[i][j])}")
    if i < len(all_matrix) - 1:
        print('-'*45)

sum_ = sum(sum(row) for matrix in all_matrix for row in matrix)
print("Сума всіх елементів:", sum_)