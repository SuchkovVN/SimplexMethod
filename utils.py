import fractions as frac
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def FracToStr(fr):
    if fr.numerator != 0:
        if fr.denominator != 1:
            return f"{fr.numerator}/{fr.denominator}"
        else:
            return f"{fr.numerator}"
    else:
        return "0"

def PrintTable(Table):
    str_row = ""
    str_row += FracToStr(Table[0][0]) + " | "
    for i in range(1, len(Table[0])):
        str_row += FracToStr(Table[0][i]) + ' '
    print(str_row)
    print("-" * len(str_row))
    for i in range(1, len(Table)):
        str_row = ""
        str_row += FracToStr(Table[i][0]) + " | "
        for j in range(1, len(Table[i])):
            str_row += FracToStr(Table[i][j])
            str_row += ' '
        print(str_row)

def InitMatrix(A,B,C):
    Matrix = []
    for i in range(len(A)):
        A[i]=[-x for x in A[i]]
    while (len(A[0])>len(C)):
        C.append(0)
    C.insert(0, 0)
    Matrix.append(C)
    for i in range(len(A[0])):
        string = []
        for j in range(len(C)):
            if (j-1 == i):
                string.append(1)
            else:
                string.append(0)
        Matrix.append(string)
    for i in range(len(A)):
        A[i].insert(0,B[i])
        Matrix.append(A[i])
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            Matrix[i][j] = frac.Fraction(str(Matrix[i][j]))
    return Matrix

def gauss_step(simplex_table, r, s):
    simplex_table[:, s] /= simplex_table[r, s]
    target_str = simplex_table[:, s]
    I = list(range(np.shape(simplex_table)[1]))
    I.remove(s)
    for i in I:
        simplex_table[:, i] -= target_str * simplex_table[r, i]
    return simplex_table


def PlotRestrictions(A, B, C):
    
    for i in range(len(B)):
        if (A[i][1] != 0):
            xs = [-5, 5]
            plt.plot(xs, [(-A[i][0] / A[i][1] * x + B[i] / A[i][1]) for x in xs], 'b-')
        elif (A[i][0] != 0):
            plt.plot([B[i] / A[i][0]] * 2, [B[i] / A[i][0], B[i] / A[i][0] * 10], 'b-')
        else:
            plt.plot(0, 0, 'bo')
    
    if (C[1] != 0):
        xs = [0, 10]
        plt.plot(xs, [(-C[0] / C[1] * x) for x in xs], 'r-')
    elif (C[0] != 0):
        plt.plot([0, 0], [0, 10], 'r-')
    else:
        plt.plot(0, 0, 'bo')
    