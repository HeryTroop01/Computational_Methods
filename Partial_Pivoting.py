#Solve the Linear Equations by: Gauss Elimination Method:

#Module used Numpy
import numpy as np

Defined Function
def partial_pivot(A, b):
    n = len(A)
    A = A.astype(float)
    b = b.astype(float)

    #Iteration_01
    for k in range(n - 1):
        #Finding the Max Value of the each row
        max_row = np.argmax(np.abs(A[k:, k])) + k

        #Condition_01
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]
            b[[k, max_row]] = b[[max_row, k]]

        #Iteration_02
        for i in range(k + 1, n):
            f = A[i, k] / A[k, k]
            A[i, k:] -= f * A[k, k:]
            b[i] -= f * b[k]

    x = np.zeros(n)

    #Iteration_03
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x
    
#Example Input of the Linear Questions
A = np.array([[6, 2, 3],
              [1, 3, 4],
              [2, 1, 3]])
b = np.array([5, 14, 13])

#Call Function
x = partial_pivot(A.copy(), b.copy())
print(x)
