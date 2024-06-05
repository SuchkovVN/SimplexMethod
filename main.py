import numpy as np
import utils
from simplex import Simplex

A = [[1, 1], [1, -1], [1, 8]]
B = [6, 1, 7]
C = [1, 1]
D = utils.InitMatrix(A, B, C)
print("Начальная таблица: ")
utils.PrintTable(D)
print("Симплекс метод: ")
D = Simplex(np.array(D))
print("Результат: ")
utils.PrintTable(D)
