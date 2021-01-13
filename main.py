import numpy as np

matr = np.array([[0, 0.2, 0.8],
                [0.5, 0, 0.5],
                [0, 0.3, 0.7]])

print('матрица перехода')
print(matr)
matr = np.linalg.matrix_power(matr, 8)
print('матрица в степени 8')
print(matr)
vec = np.array([1, 0, 0])
print('вероятности через 8 дней')
print(vec.dot(matr))
print('вероятности через большое колличество дней')
print(vec.dot(np.linalg.matrix_power(matr, 99999)))

matr = np.array([[0, 0.2, 0.8],
                [0.5, 0, 0.5],
                [0, 0.3, 0.7]])

# сколько раз покажут за 8 дней
prob = 0.0
for i in range(2, 9):
    prob += vec.dot(np.linalg.matrix_power(matr, i))[2]
print(prob)