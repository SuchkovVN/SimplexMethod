import fractions as frac
import numpy as np
import utils

def Simplex(simplex_table):
    s = np.argmax(simplex_table[0, 1:]) + 1
    k = 0
    while simplex_table[0, s] > 0:
        k += 1
        if np.min(simplex_table[:, s]) < 0:
            tmp = np.array([simplex_table[:, 0], simplex_table[:, s]])
            tmp_r = np.where(simplex_table[0:, s] < 0)[0]
            r = np.argmin(np.abs(tmp[0, tmp_r] / tmp[1, tmp_r]))
            r = tmp_r[r]
            simplex_table = utils.gauss_step(
                simplex_table, r, s
            )
        else:
            print("Целевая функция не ограничена")
            return []
        s= np.argmax(simplex_table[0, 1:]) + 1
        print(f"Шаг {k}:")
        utils.PrintTable(simplex_table)

    return simplex_table.tolist()